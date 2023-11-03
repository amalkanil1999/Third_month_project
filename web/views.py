from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    context={
        "title": "CLOTHING"
    }
    return render(request, 'index.html',context=context)


def detailed(request):
    context={
        "title": "CLOTHING | detailed"
    }
    return render(request,'detailed.html',context=context)