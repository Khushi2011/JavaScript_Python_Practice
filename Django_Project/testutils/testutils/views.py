# created by Khushi Doshi on 1st June 2021
from django.http import HttpResponse
from django.shortcuts import render


def name(request):
    my_dic = {'name1': 'Khushi', 'age': 20, 'hobby': 'book reading'}
    return render(request, 'index.html', my_dic)

# def about(request):
#     return HttpResponse("<h1>my age is 20</h1>")

# def displayFiles(request):
#     fo=open("demo.txt")
#     for x in fo:
#         f1=fo.readlines()
#         return HttpResponse(f1)


def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charCount = request.POST.get('charcount', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    params = {}
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(spaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            # else:
            #     print("no")
        # print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # print(params)
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charCount == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
            analyzed = analyzed + char
            count += 1
        analyzed = count
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed

    return render(request, 'analyze.html', params)
