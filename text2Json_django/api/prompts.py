CREATE_JSON_PROMPTS = {
    "gpt-3.5-turbo": "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else.",
    "gpt-4-1106-preview": "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else.",
}

CREATE_HIGH_DETAIL_JSON_PROMPTS = {
    "gpt-3.5-turbo": "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",
    "gpt-4-1106-preview" : "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",

}

UPDATE_JSON_PROMPTS = {
    "gpt-3.5-turbo": "You will be given two inputs following this command, first is the a json string and second is a paragraph to update in the json string. The json tree is a knowledge tree which puts the information in a form of heirarchial structure, making the information text into a granular level json representation. Your task is to take in the existing json text and append the new paragraph given into the form of json representation into the existing json. You cannot lose information of the old json. Following are the paragraph and json.",
    # Add more prompts as needed
}