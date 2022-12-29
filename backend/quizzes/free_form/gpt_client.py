import os
import threading
import time
from typing import Optional

from openai import OpenAI, OpenAIError, RateLimitError

from common.env import env
from models.pronounce import Pronounce
from tests.quizzes.free_form.fake_gpt_client import fake_ask_gpt

client = None

GPT_TIMEOUT_SECONDS = 10


def _call_completions_api(messages) -> Optional[str]:
    global client
    if not client:
        client = OpenAI(
            api_key=os.environ.get("HUPRES_OPENAI_API_KEY"),
        )

    try:
        # Start a conversation
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )
        print("GPT response", response)
        return response.choices[0].message.content
        # time.sleep(1)
        # return "Тестова відповідь"
    except RateLimitError as e:
        print("Rate limited calling OpenAI API")
        print(e)
        return f"Будь ласка, спробуйте пізніше"
    except OpenAIError as e:
        print("Error calling OpenAI API")
        print(e)
        return f"Вибачте, але я не розумію запитання"
    except TimeoutError as e:
        print("Timeout calling OpenAI API")
        print(e)
        return f"Будь ласка, спробуйте ще раз"


def _threaded_api_call(messages, response_container):
    response_container.append(_call_completions_api(messages))


def _call_completions_api_with_timeout(messages, timeout_seconds=GPT_TIMEOUT_SECONDS):
    # Container to hold the response
    response_container = []

    # Create a thread to run the API call
    thread = threading.Thread(target=_threaded_api_call, args=(messages, response_container))

    # Start the thread
    thread.start()

    # Wait for the specified timeout
    thread.join(timeout_seconds)

    # Check if thread is still alive (timeout exceeded)
    if thread.is_alive():
        # Here, implement your logic to handle the timeout scenario
        # For example, you might log a message or set a specific value in response_container
        print("GPT API call timed out")
        # It's not safe to kill a thread in Python, so you might need to handle this in another way

    # Return the response if available
    return response_container[0] if response_container else f"Будь ласка, спробуйте ще раз"


def _real_ask_gpt(respondent_summary: str, free_form_question: str, respondent_name: str, pronounce: Pronounce):
    if pronounce == Pronounce.HE_HIM:
        whom = "Його"
        whose = "нього"
    elif pronounce == Pronounce.SHE_HER:
        whom = "Її"
        whose = "неї"
    else:
        whom = "Їх"
        whose = "них"

    gpt_response = _call_completions_api_with_timeout(
        messages=[
            {
                "role": "system",
                "content": f"Ви HR-консультант з досвідом роботи у консультуванні 15 років. Ви провели тестування "
                           f"співробітника нашої компанії. {whom} звати {respondent_name}. "
                           f"З результатів тестування ви знаєте про {whose} наступне: \n{respondent_summary}\n"
                           f"Використовуйте цю інформацію для інформування відповідей на наступні запитання. "
                           f"Пам'ятайте, що відповіді повинні бути короткими і зрозумілими. "
                           f"Відповідайте тільки на запитання стосовно данного працівника. "
                           f"Якщо питання не стосується тестуванная та цього працівника, не відповідайте на нього. "
                           f"Відповідайте виключно українською мовою, навіть якщо вас питають російською чи "
                           f"англійською. І пам'ятайте що ви не GPT модель, а людина яка працює HR-консультантом."
            },
            {
                "role": "user",
                "content": f"{free_form_question}"
            },
        ]
    )
    return gpt_response


ask_gpt = _real_ask_gpt if env.is_not_test() else fake_ask_gpt
