from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.views.generic import ListView, DetailView



menu=[{'title':"О сайте",'url_name':'about'},
      {'title':"Играть",'url_name':'play'},
      {'title':"Топ игроков",'url_name':'ScoreList'},
      {'title': "О сайте", 'url_name': 'about'},
      {'title':"Войти",'url_name':'login'},

      ]


class ChessHome(ListView):
    model = masters
    template_name = 'chess/index.html' # для того чтобы класс ссылался на наш шаблон
    context_object_name = 'posts' # Для того чтобы сайт использовал нашу переменную в шаблоне
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs): #чтобы передать в класс денамический спиоск
        context = super().get_context_data(**kwargs) # распаковка словаря
        context['menu']= menu                       # Добавляем наше меню в словарь
        return context

    def get_queryset(self):                        # чтобы отображать не все статьи а только которые опубликованы
        return masters.objects.filter(is_published=True)

# def index(request):
#     posts=masters.objects.all()
#     cats=Category.objects.all()
#     context={
#         'posts': posts,
#         'cats':cats,
#         'title': 'Главная страница',
#         'menu': menu,
#         'cat_selected':0,
#     }
#     return render(request,'chess/index.html',context=context)


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

class ChessCategory(ListView):
    model = masters
    template_name = 'chess/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return masters.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat
        context['menu']= menu
        return context

# def show_category(request,cat_slug):
#     cat = Category.objects.filter(slug=cat_slug)
#     posts = masters.objects.filter(cat_id=cat[0].id)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'title': 'Отображение по рубрикам',
#         'menu': menu,
#         'cat_selected': cat[0].id,
#     }
#     return render(request, 'chess/index.html', context=context)