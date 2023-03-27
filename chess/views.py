from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *




menu=[{'title':"О сайте",'url_name':'about'},
      {'title':"Играть",'url_name':'play'},
      {'title':"Топ игроков",'url_name':'ScoreList'},
      {'title':"Войти",'url_name':'login'},

      ]

def index(request):
    posts=masters.objects.all()
    cats=Category.objects.all()
    context={
        'posts': posts,
        'cats':cats,
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected':0,
    }
    return render(request,'chess/index.html',context=context)


def ScoreList(request):
    posts = masters.objects.all()
    return render(request,'chess/TopScore.html',{'posts':posts ,'title': 'Топ', 'menu': menu,})

def login(request):
    return HttpResponse("login")

def play(request):
    return HttpResponse("play")

def about(request):
    return HttpResponse("about")

def show_post(request,post_id):
    return HttpResponse(f"post number= {post_id}")

def show_category(request,cat_id):
    posts = masters.objects.filter(cat_id=cat_id)
    if len(posts)==0:
        raise Http404()
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'chess/index.html', context=context)
