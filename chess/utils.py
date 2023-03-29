from .models import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Играть", 'url_name': 'play'},
        {'title': "Топ игроков", 'url_name': 'ScoreList'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Войти", 'url_name': 'login'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):  # создаёт контекст для шаблона
        context = kwargs  # начальный словарь
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
