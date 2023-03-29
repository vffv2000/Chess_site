from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *




menu=[{'title':"О сайте",'url_name':'about'},
      {'title':"Играть",'url_name':'play'},
      {'title':"Топ игроков",'url_name':'ScoreList'},
      {'title': "О сайте", 'url_name': 'about'},
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
    posts = masters.objects.all()
    return render(request, 'chess/play.html', {'posts': posts, 'title': 'Топ', 'menu': menu, })

def about(request):
    posts = masters.objects.all()
    return render(request,'chess/about.html',{'posts':posts ,'title': 'Топ', 'menu': menu,})

def show_post(request,post_slug):
    post = get_object_or_404(masters, slug=post_slug)

    context={
        'post': post,
        'title': post.title,
        'menu': menu,
        'cat_selected': post.cat_id,
    }
    return render(request,'chess/post.html', context=context)

def show_category(request,cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = masters.objects.filter(cat_id=cat[0].id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'cat_selected': cat[0].id,
    }
    return render(request, 'chess/index.html', context=context)