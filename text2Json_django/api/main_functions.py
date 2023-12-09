from . import openai_calls 


def createGraphFromText_(text):
    query_prompt = "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else."
    prompt = query_prompt + "\n\n Text: " + text + "\n\nJSON:"
    response = openai_calls.ask_chatgpt(prompt)
    return str(response)

def addToGraphFromText_(text, json_text):
    query_prompt = "The user will provide a JSON string, which contains the current summary in a JSON tree format. The user will then provide a field Text, which shall be used to update the graph based on this new information. You must understand the Text To Be Added, and update the JSON format provided with this new information. You can either add a new node, or modify existing JSON nodes. Your task is to take in the existing json text and append the new paragraph given into the form of json representation into the existing json. You must lose minimal information of the old json. Return ONLY in JSON format. Nothing else."
#     query_prompt="You will be given two inputs following this command, first is the a json string and second is a paragraph to update in the json string. The json tree is a knowledge tree which puts the information in a form of heirarchial structure, making the information text into a granular level json representation. Your task is to take in the existing json text and append the new paragraph given into the form of json representation into the existing json. You cannot lose information of the old json. Following are the paragraph and json."
    prompt = query_prompt + "\n\n Paragraph : " + text + "\n\nJSON: " + json_text + " \n\nUpdated JSON:"
    response = openai_calls.ask_chatgpt(prompt)
    return str(response)

