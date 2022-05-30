from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Image
# Create your views here.
# def home(request):
#     return HttpResponse("hello world")
def home(request):
    welcome="Hello! Welcome to Memory Bubbles."
    images = Image.objects.order_by('-published')
    categories = Image.objects.order_by('image_category')
    locations = Image.objects.order_by('image_location')

    return render(request,'index.html', {'welcome':welcome,'images':images,'categories':categories,'locations':locations})

def search(request):
    if 'images' in request.GET and request.GET['images']:
        #check if the image query exists in our request.GET object and then we then check if it has a value
        search_term = request.GET.get('images')
        searched_images=Image.search_image(search_term)
        message=f'{search_term} '
        return render(request,'search.html',{'searched_images':searched_images,'message':message})
    else:
        message='Try searching for something'
        return render(request,'search.html',{'message':message})

def image(request):
    try:
        image=Image.get_image_by_id()
    except Image.DoesNotExist:
        raise Http404()
    return render(request,'image.html',{'image':image} )
