CREATE_JSON_PROMPTS = {
    "gpt-3.5-turbo": "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else.",
    "gpt-4-1106-preview": "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else.",
    "gpt-4":"You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else.",

}

CREATE_HIGH_DETAIL_JSON_PROMPTS = {
    "gpt-3.5-turbo": "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",
    "gpt-4-1106-preview" : "You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",
    "gpt-4":"You are a assigned a task to build a knowledge graph. Based on the text provided you have to create a JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",
}
COMBINE_JSON_SUMMARIES = {
    "gpt-3.5-turbo": "You will be give list of JSON separated by '|||'. Please remember to treat separate JSONs based on separator '|||'. Each JSON signifies a knowledge graph of part of bigger text broken down into chunks. You are a assigned a task to build a merged knowledge graph. Based on the JSON list provided you have to create a combined JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Your task is to merge the JSONs and create one merged JSON. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",
    "gpt-4-1106-preview" : "You will be give list of JSON separated by '|||'. Please remember to treat separate JSONs based on separator '|||'. Each JSON signifies a knowledge graph of part of bigger text broken down into chunks. You are a assigned a task to build a merged knowledge graph. Based on the JSON list provided you have to create a combined JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Your task is to merge the JSONs and create one merged JSON. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL.",
    "gpt-4" : "You will be give list of JSON separated by '|||'. Please remember to treat separate JSONs based on separator '|||'. Each JSON signifies a knowledge graph of part of bigger text broken down into chunks. You are a assigned a task to build a merged knowledge graph. Based on the JSON list provided you have to create a combined JSON output such that key will represent all the significant elements of the text and values would represent the summary of key. Your task is to merge the JSONs and create one merged JSON. Break down the values into more granular level information creating a tree or graph based hierarchy. Only output JSON format. Nothing else. Please make sure that the tree is as deep as possible, you must break down as much information as possible. If a choice arises between breaking down information or not, always break down the information into multiple node. You must capture ALL the infroamtion in the text - and most of this information should be near the leaves. Keep the nodes brief, but the leaved long and more information rich. Furthermore, if the text is a fiction book, do not simply use the chapters as nodes- actually break down the story into characters, important events etc. Additionally, if the input is a scientific text or a report, make sure that your tree covers all the ionformation in the leaf, and is readable so anyone can easily understand scientific literature. Remember - HIGH DETAIL."

}

UPDATE_JSON_PROMPTS = {
    "gpt-3.5-turbo": "The user will provide a JSON string, which contains the current summary in a JSON tree format. The user will then provide a field Text, which shall be used to update the graph based on this new information. You must understand the Text To Be Added, and update the JSON format provided with this new information. You can either add a new node, or modify existing JSON nodes. Your task is to take in the existing json text and append the new paragraph given into the form of json representation into the existing json. You must lose minimal information of the old json. Return ONLY in JSON format. Nothing else.",
   "gpt-4-1106-preview": "The user will provide a JSON string, which contains the current summary in a JSON tree format. The user will then provide a field Text, which shall be used to update the graph based on this new information. You must understand the Text To Be Added, and update the JSON format provided with this new information. You can either add a new node, or modify existing JSON nodes. Your task is to take in the existing json text and append the new paragraph given into the form of json representation into the existing json. You must lose minimal information of the old json. Return ONLY in JSON format. Nothing else..",
    "gpt-4" :"The user will provide a JSON string, which contains the current summary in a JSON tree format. The user will then provide a field Text, which shall be used to update the graph based on this new information. You must understand the Text To Be Added, and update the JSON format provided with this new information. You can either add a new node, or modify existing JSON nodes. Your task is to take in the existing json text and append the new paragraph given into the form of json representation into the existing json. You must lose minimal information of the old json. Return ONLY in JSON format. Nothing else..",
    # Add more prompts as needed
}

TRAVERSE_GRAPH_PROMPTS = {
    "gpt-4-1106-preview" : '''You are a machine which will assist in graph traversal. You will be given
1. A query, which is looking for the node which is most relevant to the query
2. Current Node : the current node description
3. Children Nodes : all the descriptions of the children nodes of the current node

You are required to answer the following 2 questions :

1. Is the current node more relevant than any of the children nodes : the answer is "Yes" or "No". Only output "No" if a child node is clearly more relevant to the query. Say "Yes" in cases where the query is more general, and the current node is a good way to summarize the query.

2. Which of the children nodes is most relevant : The answer is the exact text of the children nodes

Your output should be in the form of a JSON, such as 

Sample Query 1: How much sugar should I add while baking cake?
Sample Node 1: Cooking Techniques
Sample Children Nodes :1 Frying Techniques, Baking Techniques",  Chopping Techniques

Sample Answer 1: {"IsCurrentNodeMostRelevant":"No" , "MostRelevantChildNode":"Baking Techniques"}

Sample Query 2: What was the effect on french economy
Sample Node 2: Economic Crises
Sample Children Nodes : Bread Shortage, No homes, High taxation , High inflation

Sample Answer 2: {"IsCurrentNodeMostRelevant":"Yes" , "MostRelevantChildNode":"High inflation"}

Only output the JSON, no other information. The "IsCurrentNodeMostRelevant" must only be "Yes" or "No", and the "MostRelevantChildNode" must have the exact text from the Sample Children Nodes.

Sample Query 3: How to properly mix flour and water
Sample Node 3: Ingredients
Sample Children Nodes : Dough, Toppings

Sample Answer 3 :{"IsCurrentNodeMostRelevant":"No", "MostRelevantChildNode":"Dough"} 

''',
"gpt-4":'''You are a machine which will assist in graph traversal. You will be given
1. A query, which is looking for the node which is most relevant to the query
2. Current Node : the current node description
3. Children Nodes : all the descriptions of the children nodes of the current node

You are required to answer the following 2 questions :

1. Is the current node more relevant than any of the children nodes : the answer is "Yes" or "No". Only output "No" if a child node is clearly more relevant to the query. Say "Yes" in cases where the query is more general, and the current node is a good way to summarize the query.

2. Which of the children nodes is most relevant : The answer is the exact text of the children nodes

Your output should be in the form of a JSON, such as 

Sample Query 1: How much sugar should I add while baking cake?
Sample Node 1: Cooking Techniques
Sample Children Nodes :1 Frying Techniques, Baking Techniques",  Chopping Techniques

Sample Answer 1: {"IsCurrentNodeMostRelevant":"No" , "MostRelevantChildNode":"Baking Techniques"}

Sample Query 2: What was the effect on french economy
Sample Node 2: Economic Crises
Sample Children Nodes : Bread Shortage, No homes, High taxation , High inflation

Sample Answer 2: {"IsCurrentNodeMostRelevant":"Yes" , "MostRelevantChildNode":"High inflation"}

Only output the JSON, no other information. The "IsCurrentNodeMostRelevant" must only be "Yes" or "No", and the "MostRelevantChildNode" must have the exact text from the Sample Children Nodes.

Sample Query 3: How to properly mix flour and water
Sample Node 3: Ingredients
Sample Children Nodes : Dough, Toppings

Sample Answer 3 :{"IsCurrentNodeMostRelevant":"No", "MostRelevantChildNode":"Dough"} 

''',
}

ANSWER_FROM_GRAPH_PROMPTS = {
    "gpt-4-1106-preview" :"You are a question answering machine. You will be provided a tree, in the form of a JSON. You must understand that tree, and answer a question based on the tree. Use ONLY the information available in the tree to answer the question, DO NOT HALLUCINATE ANSWERS. In case the answer cannot be answered at all based of the tree reply - I cannot answer this question based on the tree or summary provided to me.",
    "gpt-4":"You are a question answering machine. You will be provided a tree, in the form of a JSON. You must understand that tree, and answer a question based on the tree. Use ONLY the information available in the tree to answer the question, DO NOT HALLUCINATE ANSWERS. In case the answer cannot be answered at all based of the tree reply - I cannot answer this question based on the tree or summary provided to me."

}