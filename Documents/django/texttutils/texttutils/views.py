#i have create this file----Prince
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     myd={
#         'name':'Prince',
#         'place':'Mars'
#     }
#     return render(request,'index.html',myd)
#     # return HttpResponse('''
#     # <a href='https://developer.mozilla.org/en-US/docs/Web/JavaScript'>JavaScript</a><br>
#     # <a href='https://www.djangoproject.com/'>Django</a><br>
#     # <a href='https://getbootstrap.com/'>Bootstrap</a><br>
#     # <a href='https://www.python.org/'>Python</a><br>''')
# def about(request):
#     return HttpResponse('About Prince')

# def display(request):
#     f=open('1.txt')
#     content=f.read()
#     return HttpResponse(content)

def index(request):
    return render(request,'index.html')
def analyze(request):
    
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')
    
    if (removepunc=='on'):
        analysis=""
        punc='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char  not in punc:
                analysis+=char
        context={
            'punc': analysis
        }
        djtext=analysis
        #Analyze the text
        # return render(request,'analyze.html',context)
    if(fullcaps=='on'):
        analysis=""
        for char in djtext:
            analysis+=char.upper()
        context={
            'punc': analysis
        }
        djtext=analysis
        #Analyze the text
        # return render(request,'analyze.html',context)

    if(newlineremove=='on'):
        analysis=""
        for char in djtext:
            if char!='\n' and char!='\r':
             analysis+=char
        context={
            'punc': analysis
        }
        djtext=analysis
        #Analyze the tPOST
        # return render(request,'analyze.html',context)
    if(spaceremove=='on'):
        analysis=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analysis = analysis + char

        context={
            'punc': analysis
        } 
        djtext=analysis
        #Analyze the text
        # return render(request,'analyze.html',context)
    if removepunc == 'on' or fullcaps == 'on' or newlineremove == 'on' or spaceremove == 'on':
        return render(request,'analyze.html',context)
    else:
        return HttpResponse('Error!!')
# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")