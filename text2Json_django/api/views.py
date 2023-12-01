from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from . import main_json2tree
import requests
# import main_functions
from . import main_functions

@csrf_exempt
@require_POST
def joinText(request):
    data = request.POST
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    return JsonResponse({'result': text1 + text2})

@csrf_exempt
@require_POST
def callOpenAI(request):
    data = request.POST
    question = data.get('question', '')
    return JsonResponse({'answer': 'response from OpenAI'})

@csrf_exempt
@require_POST
def createGraphFromText(request):
    data = json.loads(request.body)
    text = data.get('text', '')
    response_json = main_functions.createGraphFromText_(text)
    # response_json = '''{'French Revolution': {'Summary': 'A period of political and societal change in France that began in 1789 and ended in 1799, resulting in the formation of the French Consulate. It had significant impact on liberal democracy and remains central to French political discourse.', 'Ideas': {'Fundamental Principles of Liberal Democracy': 'Many ideas of the French Revolution are considered to be fundamental principles of liberal democracy.', 'Values and Institutions': 'The values and institutions of the French Revolution continue to be central to modern French political discourse.'}, 'Causes': {'Factors': 'The causes of the French Revolution are a combination of social, political, and economic factors.', 'Inability to Manage': 'The Ancien Régime proved unable to manage the crisis.', 'Financial Crisis': 'A financial crisis and widespread social distress in May 1789 led to the convocation of the Estates General.', 'Radical Measures': 'The Storming of the Bastille on 14 July led to a series of radical measures by the Assembly, including the abolition of feudalism, state control over the Catholic Church in France, and a declaration of rights.'}, 'Events': {'Insurrection of 10 August 1792': 'A series of military defeats resulted in the Insurrection of 10 August 1792, leading to the abolition of the monarchy and the establishment of the French First Republic.', 'Reign of Terror': 'After a Paris-based revolt in June 1793, the constitution was suspended and political power passed to the Committee of Public Safety, resulting in the Reign of Terror and the execution of thousands of individuals.', 'Replacement of the Republic': 'The weakened Republic was replaced by the Directory in November 1795.', 'Coup led by Napoleon Bonaparte': 'In November 1799, the Consulate seized power in a military coup led by Napoleon Bonaparte, marking the end of the Revolutionary period.'}, 'Long-Term Factors': {'Population Growth': 'Between 1715 and 1789, the French population grew from an estimated 21 to 28 million, with the proportion of the population living in towns increasing to 20%.', 'Growing Middle Class': 'The middle classes tripled over the century, reaching almost 10% of the population by 1789.', 'Increasing Inequality': 'Increasing inequality led to more social conflict as the century progressed.', 'Uneven Distribution of Prosperity': "The benefits of increasing prosperity were distributed unevenly across regions and social groups, with those benefiting the most being involved in agriculture, rents, interest, and trade in goods from France's slave colonies.", 'Economic Recession and Bad Harvests': 'Economic recession from 1785 and bad harvests in 1787 and 1788 led to high unemployment and food prices, coinciding with a financial and political crisis for the monarchy.'}, 'Short-Term Factors': {'Debt Crisis': "The French state experienced a debt crisis, although the level of debt itself was not high compared to Britain's.", 'Taxation System': 'The tax rates varied widely, causing uncertainty and resentment among taxpayers. Attempts to simplify the system were blocked by the regional Parlements.', "Louis XVI's Opposition": 'Louis XVI often backed down when faced with opposition from conservative elements within the nobility.', 'Enlightenment and Public Debate': 'Enlightenment critiques of social institutions and public debates inspired by the American Revolution and European revolts of the 1780s shaped the response of the educated French elite to the crisis facing the state.', 'Public Scandals': 'Public scandals, such as the Diamond Necklace Affair, fueled popular anger at the court, nobility, and church officials.'}}}'''
    
    print("response_json : ", response_json)
    texty = main_json2tree.generate(response_json)
    # print("texty = ", texty)
    return JsonResponse({'response': texty})

@csrf_exempt
@require_POST
def addToGraphFromText(request):
    data = json.loads(request.body)
    text = data.get('text', '')
    json_text = data.get('json_text', '')
    response_json = main_functions.addToGraphFromText_(text, json_text)
    
    return JsonResponse({'response': 'response_json'})