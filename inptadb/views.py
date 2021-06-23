from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = dict()
    return render(request, 'inptadb/index.html', context)
    #return HttpResponse("Welcome to InPTA!")
