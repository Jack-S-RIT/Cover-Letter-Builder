import os
import re
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

MAX_TOKENS = 350


def split_paragraphs(input_text=""):
    newlines_re = re.compile(r"\n{2,}")  # two or more "\n" characters
    no_newlines = input_text.strip("\n")  # remove leading and trailing "\n"
    split_text = newlines_re.split(no_newlines)  # regex splitting
    paragraphs = [p + "\n" for p in split_text if p.strip()]
    # p + "\n" ensures that all lines in the paragraph end with a newline
    # p.strip() == True if paragraph has other characters than whitespace
    return paragraphs


def generate_default_cover_letter_prompt(position, company):
    return """
    write a cover letter for the position of a {0} for the company {1}
    """.format(position.capitalize(), company.capitalize()
               )


def generate_default_cover_letter_response(position, company):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_default_cover_letter_prompt(position, company),
        temperature=0.25,
        max_tokens=MAX_TOKENS,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response
