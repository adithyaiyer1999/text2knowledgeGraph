from . import openai_calls 
from . import prompts

def createGraphFromText_(text):
    model = "gpt-3.5-turbo"
    query_prompt = prompts.CREATE_JSON_PROMPTS[model]
    prompt = query_prompt + "\n\n Text: " + text + "\n\nJSON:"
    response = openai_calls.ask_chatgpt(prompt)
    return str(response)

def addToGraphFromText_(text, json_text):
    model = "gpt-3.5-turbo"
    query_prompt = prompts.UPDATE_JSON_PROMPTS[model]
    prompt = query_prompt + "\n\n Paragraph : " + text + "\n\nJSON: " + json_text + " \n\nUpdated JSON:"
    response = openai_calls.ask_chatgpt(prompt)
    return str(response)

