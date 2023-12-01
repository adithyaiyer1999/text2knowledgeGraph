from . import openai_calls 


def createGraphFromText_(text):
    query_prompt = "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else."
    prompt = query_prompt + "\n\n Text: " + text + "\n\nJSON:"
    response = openai_calls.ask_chatgpt(prompt)
    return str(response)

def addToGraphFromText_(text, json_text):
    query_prompt = "The user will provide a JSON string, which contains the current summary in a JSON tree format. The use will then provide a field Text To Be Added. You must understand the Text To Be Added, and update the JSON format provided with this new information. Return ONLY in JSON format. Nothing else." 
    prompt = query_prompt + "\n\n Text To Be Added: " + text + "\n\nJSON: " + json_text + " \n\nUpdated JSON:"
    response = openai_calls.ask_chatgpt(prompt)
    return str(response)

