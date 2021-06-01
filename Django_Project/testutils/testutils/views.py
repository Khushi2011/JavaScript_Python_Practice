#created by Khushi Doshi on 1st June 2021 
from django.http import HttpResponse
from django.shortcuts import render
def name(request):
    my_dic={'name1':'Khushi','age':20,'hobby':'book reading'}
    return render(request,'index.html',my_dic)

# def about(request):
#     return HttpResponse("<h1>my age is 20</h1>")

# def displayFiles(request):
#     fo=open("demo.txt")
#     for x in fo:
#         f1=fo.readlines()
#         return HttpResponse(f1)
    
def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")