from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('',index, name = 'home'),
    path('Top/', ScoreList ,name= 'ScoreList'),
    path('login/',login,name= 'login'),
    path('play/',play,name= 'play'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/',show_post,name='post'),
    path('category/<int:cat_id>/',show_category,name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)