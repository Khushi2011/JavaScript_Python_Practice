#created by Khushi Doshi on 1st June 2021 
from django.http import HttpResponse
from django.shortcuts import render
def name(request):
    my_dic={'name1':'Khushi','age':20,'hobby':'book reading'}
    return render(request,'index.html',my_dic)

# def about(request):
#     return HttpResponse("<h1>my age is 20</h1>")

# def displayFiles(request):
#     fo=open(r"F:\vacationStudy2021\Django_Project\testutils\testutils\demo.txt")
#     for x in fo:
#         f1=fo.readlines()
#         return HttpResponse(f1)
def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")
        

