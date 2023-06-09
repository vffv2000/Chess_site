from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', ChessHome.as_view(), name='home'),
    path('Top/', scorelist, name='Scorelist'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('play/', play, name='play'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ChessCategory.as_view(), name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
