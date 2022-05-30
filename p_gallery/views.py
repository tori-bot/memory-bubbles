from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Image
# Create your views here.
# def home(request):
#     return HttpResponse("hello world")
def home(request):
    welcome="hello. welcome to Makena's memory bubbles."
    images = Image.objects.order_by('-published')
    categories = Image.objects.order_by('image_category')
    locations = Image.objects.order_by('image_location')

    return render(request,'index.html', {'welcome':welcome,'images':images,'categories':categories,'locations':locations})

def search(request):
    if 'images' in request.GET and request.GET['images']:
        #check if the image query exists in our request.GET object and then we then check if it has a value
        category = request.GET.get('images')
        searched_images=Image.search_image(category)
        message=f'{category} '
        return render(request,'search.html',{'searched_images':searched_images,'message':message})
    else:
        message='Try searching for something'
        return render(request,'search.html',{'message':message})

def image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,'image.html',{'image':image} )
