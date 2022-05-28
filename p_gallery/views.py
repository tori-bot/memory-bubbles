from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return HttpResponse("hello world")
def home(request):
    welcome="hello. welcome to Makena's memory bubbles."
    return render(request,'index.html', {'welcome':welcome})