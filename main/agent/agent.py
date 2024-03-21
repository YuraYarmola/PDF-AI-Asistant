from django.conf import settings
from openai import OpenAI
import logging
from .functions import *


class PDFContext:
    def __init__(self, user):
        self.user = user
        self.llm = OpenAI(
            api_key=settings.OPENAI_KEY,
        )

    def prompt(self, prompt: str) -> str:
        completion = self.llm.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a PDF Context AI helper, skilled to explaining text from PDF documents\n"
                            "Answer the question that are only in PDF\n"
                            "Say page and document where you find answer the question\n"},

                {"role": "user", "content": f"Answer: {prompt} \n PDF documents:{get_all_files_context(self.user)}"}
            ]
        )

        return completion.choices[0].message.content

