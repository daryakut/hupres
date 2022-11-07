import os

from openai import OpenAI, OpenAIError

from models.pronounce import Pronounce

client = OpenAI(
    api_key=os.environ.get("HUPRES_OPENAI_API_KEY"),
)


def ask_gpt(respondent_summary: str, free_form_question: str, respondent_name: str, pronounce: Pronounce):
    if pronounce == Pronounce.HE_HIM:
        whom = "Його"
        whose = "нього"
    elif pronounce == Pronounce.SHE_HER:
        whom = "Її"
        whose = "неї"
    else:
        whom = "Їх"
        whose = "них"

    try:
        # Start a conversation
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
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
        print("GPT response", response)
        # Return the response text
        return response.choices[0].message.content
    except OpenAIError as e:
        print("Error calling OpenAI API")
        print(e)
        return f"Вибачте, але я не розумію запитання"
