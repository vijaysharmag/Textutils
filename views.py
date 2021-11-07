from django.contrib.admin.sites import DefaultAdminSite
from django.http.response import HttpResponseNotAllowed

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("HELLO")

def about(request):
    return HttpResponse('''<h1>about</h1>
    <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django codewithharry</a>''')
    

def index(request):
    
    return render(request,'index.html',)

def ex1(request):
    return HttpResponse('''
    <h1> Personal Navigator </h1>
    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12" target="_blank"> codewithharry </a>
    ''')


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
  
    # check which  checkbox is on  
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        context = {'purpose' : 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze2.html', context)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        
        context = {'purpose' : 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', context)  

    if(newlineremover=="on"):
        analyzed =""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        context = {'purpose' : 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', context)

    if(extraspaceremover=="on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]== " "):
                analyzed = analyzed + char
        context = {'purpose' : 'Removed Newlines', 'analyzed_text': analyzed}
    
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please choose the action!")
           
   

    return render(request, 'analyze2.html', context)

# def capfirst(request):
#     return HttpResponse("capitalize first")
    
# def newlinermove(request):
#     return HttpResponse("new line remove first <a href='/'>back</a>")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount")

