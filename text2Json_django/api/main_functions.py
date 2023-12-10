from . import openai_calls 
from . import prompts
import json

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
    model = "gpt-3.5-turbo"
    query_prompt = prompts.UPDATE_JSON_PROMPTS[model]
    prompt = query_prompt + "\n\n Paragraph : " + text + "\n\nJSON: " + json_text + " \n\nUpdated JSON:"
    response = openai_calls.ask_chatgpt(prompt, model)
    str_response = str(response)
    
    # Some sanity text cleaning to avoid errors in yaml loading
    str_response = str_response.replace("json", "")
    str_response = str_response.replace("`", "")
    return str_response

def searchGraphFromText_(text, json_text):
    pathToNode, graph_dict = getMostRelevantNode(text, json_text)
    str_response = str(graph_dict)
    print("pathToNode: ", pathToNode)
    
    # Some sanity text cleaning to avoid errors in yaml loading
    str_response = str_response.replace("json", "")
    str_response = str_response.replace("`", "")
    return str_response

def getMostRelevantNode(text, json_text):
    # lets store the entire path
    pathToNode = []

    graph_dict = json.loads(json_text)
    # pathToNode.append("Start")
    current_node = "Start"
    children_nodes = list(graph_dict.keys())
    IsCurrentNodeMostRelevant = "No"

    # Lets have 2 strikes, or 2 times that the model has to say "Yes", this is the most relevant node
    strikes = 0

    while IsCurrentNodeMostRelevant == "No":
        IsCurrentNodeMostRelevant, nextNode = getNextNodeFromOpenAI(current_node, children_nodes, text)
        print("IsCurrentNodeMostRelevant: ", IsCurrentNodeMostRelevant)
        print("nextNode: ", nextNode)
        current_node = nextNode
        pathToNode.append(current_node)
        if isinstance(graph_dict[current_node], str):
            print("reached leaf node")
            break
        children_nodes = list(graph_dict[current_node].keys())
        # if we have reached the right node, reply with a graph with this node as the root
        if IsCurrentNodeMostRelevant == "Yes":
            strikes = strikes+1 
            IsCurrentNodeMostRelevant="No"
        if strikes == 2:
            break
        graph_dict = graph_dict[current_node]
        if len(children_nodes) == 0:
            break
    return pathToNode, graph_dict



def getNextNodeFromOpenAI(current_node,children_nodes, query):
    model = "gpt-4-1106-preview"
    query_prompt = prompts.TRAVERSE_GRAPH_PROMPTS[model]
    prompt = query_prompt + "\n\n Query: " + query + "\n\n Node: " + current_node + "\n\nChildren Nodes: " + sepearateListWithCommas(children_nodes) + "\n\Answer:"
    response = openai_calls.ask_chatgpt(prompt, model)
    str_response = str(response)
    
    # Some sanity text cleaning to avoid errors in yaml loading
    str_response = str_response.replace("json", "")
    str_response = str_response.replace("`", "")

    json_output = json.loads(str_response)

    return json_output["IsCurrentNodeMostRelevant"], json_output["MostRelevantChildNode"]

def sepearateListWithCommas(list):
    return ', '.join(list)




