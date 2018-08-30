from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    mydict={'insert':"Hello I am from views.py"}
    return render(request,'first/index.html',context=mydict)
# Create your views
