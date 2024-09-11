import os
import re
import json

from openai import OpenAI
from prompt import PROMPT

from dotenv import load_dotenv

import pymupdf

load_dotenv()



doc = pymupdf.open("sample-invoice.pdf")
text = ""
for page_num in range(doc.page_count):
    page = doc.load_page(page_num)  
    text += page.get_text() 
doc.close()


def createRegex(text):
    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": PROMPT},
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return completion.choices[0].message.content

def extractData(text, patterns_json):

    try:
        patterns = json.loads(patterns_json)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

    extracted_data = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_data[field] = match.group(1)
        else:
            extracted_data[field] = None

    return extracted_data


print(extractData(text, createRegex(text)))