from django.shortcuts import render

# Create your views here.
def home(request):
    welcome="hello. welcome to Makena's memory bubbles."
    return render('index.html', {'welcome':welcome})