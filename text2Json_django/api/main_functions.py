from . import openai_calls 
from . import prompts

def createGraphFromText_(text):
    model = "gpt-4-1106-preview"
    query_prompt = prompts.CREATE_HIGH_DETAIL_JSON_PROMPTS[model]
    prompt = query_prompt + "\n\n Text: " + text + "\n\nJSON:"
    response = openai_calls.ask_chatgpt(prompt, model)

    str_response = str(response)
    
    # Some sanity text cleaning to avoid errors in yaml loading
    str_response = str_response.replace("json", "")
    str_response = str_response.replace("`", "")
    return str_response

def addToGraphFromText_(text, json_text):
    model = "gpt-4-1106-preview"
    query_prompt = prompts.UPDATE_JSON_PROMPTS[model]
    prompt = query_prompt + "\n\n Paragraph : " + text + "\n\nJSON: " + json_text + " \n\nUpdated JSON:"
    response = openai_calls.ask_chatgpt(prompt, model)
    str_response = str(response)
    
    # Some sanity text cleaning to avoid errors in yaml loading
    str_response = str_response.replace("json", "")
    str_response = str_response.replace("`", "")
    return str_response

