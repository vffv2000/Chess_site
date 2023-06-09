from .models import *


menu = [
        {'title': "Играть", 'url_name': 'play'},
        {'title': "Топ игроков", 'url_name': 'Scorelist'},
        {'title': "О сайте", 'url_name': 'about'},
        ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):  # создаёт контекст для шаблона
        context = kwargs  # начальный словарь
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
