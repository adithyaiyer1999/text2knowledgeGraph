from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
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
    html_text = main_json2tree.generate(response_json)
    print("html_text: ", html_text)
    return HttpResponse(html_text, content_type="text/html")

@csrf_exempt
@require_POST
def addToGraphFromText(request):
    data = json.loads(request.body)
    text = data.get('text', '')
    json_text = data.get('json_text', '')
    response_json = main_functions.addToGraphFromText_(text, json_text)
    html_text = main_json2tree.generate(response_json)
    return JsonResponse({'response': html_text})