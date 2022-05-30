from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

  
from django.conf.urls import url

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('category/',views.category,name='category'),
    path('location/',views.location,name='location'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)