from django.http import HttpResponse
from django.shortcuts import render
from .models import Image
# Create your views here.
# def home(request):
#     return HttpResponse("hello world")
def home(request):
    welcome="hello. welcome to Makena's memory bubbles."
    return render(request,'index.html', {'welcome':welcome})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        #check if the article query exists in our request.GET object and then we then check if it has a value
        category = request.GET.get('category')
        searched_images=Image.search_image(category)
        message=f'{category} '
        return render(request,'search.html',{'searched_images':searched_images,'message':message})
    else:
        message='Try searching for something'
        return render(request,'search.html',{'message':message})