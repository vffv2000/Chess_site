from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm, LoginUserForm
from .utils import *


class ChessHome(DataMixin, ListView):

    model = Masters
    template_name = 'chess/index.html'  # для того чтобы класс ссылался на наш шаблон
    context_object_name = 'posts'  # Для того чтобы сайт использовал нашу переменную в шаблоне

    def get_context_data(self, *, object_list=None, **kwargs):  # чтобы передать в класс денамический спиcок
        context = super().get_context_data(**kwargs)  # распаковка словаря
        c_def = self.get_user_context(title='Главная страница')  # получаем инфу из нашего data-mixin
        return context | c_def  # формируем общий контект

    def get_queryset(self):  # чтобы отображать не все статьи а только которые опубликованы
        return Masters.objects.filter(is_published=True)

# def index(request):
#     posts=Masters.objects.all()
#     cats=Category.objects.all()
#     context={
#         'posts': posts,
#         'cats':cats,
#         'title': 'Главная страница',
#         'menu': menu,
#         'cat_selected':0,
#     }
#     return render(request,'chess/index.html',context=context)


def scorelist(request):
    posts = Masters.objects.all()
    return render(request, 'chess/TopScore.html', {'posts': posts, 'title': 'Топ', 'menu': menu, })


def play(request):
    posts = Masters.objects.all()
    return render(request, 'chess/play.html', {'posts': posts, 'title': 'Топ', 'menu': menu, })


def about(request):
    posts = Masters.objects.all()
    return render(request, 'chess/about.html', {'posts': posts, 'title': 'Топ', 'menu': menu, })


class ShowPost(DataMixin, DetailView):
    model = Masters
    template_name = 'chess/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def

# def show_post(request,post_slug):
#     post = get_object_or_404(Masters, slug=post_slug)
#
#     context={
#         'post': post,
#         'title': post.title,
#         'menu': menu,
#         'cat_selected': post.cat_id,
#     }
#     return render(request,'chess/post.html', context=context)


class ChessCategory(DataMixin, ListView):
    model = Masters
    template_name = 'chess/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Masters.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return context | c_def

# def show_category(request,cat_slug):
#     cat = Category.objects.filter(slug=cat_slug)
#     posts = Masters.objects.filter(cat_id=cat[0].id)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'title': 'Отображение по рубрикам',
#         'menu': menu,
#         'cat_selected': cat[0].id,
#     }
#     return render(request, 'chess/index.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'chess/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return context | c_def


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'chess/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')