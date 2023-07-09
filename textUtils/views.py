# I have created this file - Kartik Sharma
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    param = {'name':'Kartik Sharma', 'place': 'Gurugram'}
    return render(request, 'index.html', param)

def about(request):
    return HttpResponse("Hey, its me Kartik Sharma")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose' : 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'All Upper Case' , 'analyzed_text' : analyzed}
        djtext = analyzed


    if(lowercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'All Lower Case', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed


    if(spaceremove == "on"):
        analyzed = ""
        for char in djtext:
            if(char != " "):
                analyzed = analyzed + char
        params = {'purpose' : 'Remove Spaces' , 'analyzed_text' : analyzed}
        djtext = analyzed


    if (extraspaceremover == "on") :
        analyzed = ""
        for index , char in enumerate( djtext ) :
            if not (djtext[index] == " " and djtext[index + 1] == " ") :
                analyzed = analyzed + char
        params = {'purpose' : 'Remove Extra Spaces' , 'analyzed_text' : analyzed}
        djtext = analyzed


    if(charcount == "on"):
        analyzed = len(djtext.replace(" ", ""))
        params = {'purpose' : 'Count Characters' , 'analyzed_text' : analyzed}

    if(removepunc != "on" and uppercase != "on" and lowercase != "on" and newlineremove != "on" and spaceremove != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error! Please select one operations")

    return render(request, 'analyze.html', params)
