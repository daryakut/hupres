import os

import openai

from models.pronounce import Pronounce

openai.api_key = os.environ["HUPRES_OPENAI_API_KEY"]


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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Ви HR-консультант з досвідом роботи у консультуванні 15 років. Ви провели тестування "
                               f"співробітника нашої компанії. {whom} звати {respondent_name}. "
                               f"З результатів тестування ви знаєте про {whose} наступне: \n{respondent_summary}\n"
                               f"Використовуйте цю інформацію для інформування відповідей на наступні запитання. "
                               f"Пам'ятайте, що відповіді повинні бути короткими і зрозумілими. "
                               f"Відповідайте тільки на запитання стосовно данного працівника. "
                               f"Відповідайте виключно українською мовою. "
                },
                {
                    "role": "user",
                    "content": f"{free_form_question}"
                },
            ]
        )

        # Return the response text
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        print("Error calling OpenAI API")
        print(e)
        return f"Вибачте, але я не розумію запитання"
