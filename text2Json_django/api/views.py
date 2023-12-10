from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from . import main_json2tree
from PyPDF2 import PdfReader
import requests
# import main_functions
from . import main_functions
from . import main_graphmanipulations
from . import constants

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
    if len(text)>constants.THRESHOLD_FOR_ITERATIVE_UPDATE:   # This signifies that our text is very big and needs an iterative function to handle this
        print("Entered the iterative Text->JSON")
        response_json = main_functions.createGraphFromTextIteratively_(text)  # We need to create chunks and summarize iteratively
    else:
        print("Entered the normal Text->JSON")
        response_json = main_functions.createGraphFromText_(text)
    request.session['response_json'] = response_json
    print("response_json = ",response_json)
    print("request.session:",request.session)
    html_text = main_json2tree.generate(response_json)
    print("html_text: ", html_text)
    request.session.save()
    return HttpResponse(html_text, content_type="text/html")

@csrf_exempt
@require_POST
def createGraphFromPdf(request):
    # First let's create a text file from the pdf
    file = request.FILES.get('file')
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    # Now let's call the createGraphFromText function
    response_json = main_functions.createGraphFromText_(text)
    request.session['response_json'] = response_json
    html_text = main_json2tree.generate(response_json)
    print("html_text: ", html_text)
    request.session.save()
    return HttpResponse(html_text, content_type="text/html")

@csrf_exempt
@require_POST
def addToGraphFromText(request):
    data = json.loads(request.body)
    text = data.get('text', '')
    print(request.session.get('response_json'))
    response_json = request.session.get('response_json')
    print("response_json:",response_json)
    if response_json is not None:
        updated_response_json = main_functions.addToGraphFromText_(text, response_json)
        changed_color_updated_json=main_graphmanipulations.find_difference_change_color(response_json,updated_response_json)
        html_text = main_json2tree.generate(str(changed_color_updated_json))
        return HttpResponse(html_text, content_type="text/html")
    else:
         # Handle the case where response_json is not in session
        return JsonResponse({'error': 'Previous graph data not found'})
    
@csrf_exempt
@require_POST
def searchGraphFromText(request):
    data = json.loads(request.body)
    text = data.get('text', '')
    response_json = request.session.get('response_json')
    if response_json is not None:
        response_json_smol = main_functions.searchGraphFromText_(text, response_json)
        # changed_color_updated_json=main_graphmanipulations.find_difference_change_color(response_json,updated_response_json)
        html_text = main_json2tree.generate(str(response_json_smol))
        request.session['response_json_smol'] = response_json_smol
        return HttpResponse(html_text, content_type="text/html")
    else:
         # Handle the case where response_json is not in session
        return JsonResponse({'error': 'Previous graph data not found'})