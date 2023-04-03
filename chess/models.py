from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Chess(models.Model):
    Username = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Games = models.CharField(max_length=255, default=0)
    Wins = models.CharField(max_length=255, default=0)
    Loses = models.CharField(max_length=255, default=0)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Masters(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name="Категории")
    user = models.ForeignKey(User,verbose_name='Пользователь',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Известные шахматисты"
        verbose_name_plural = "Известные шахматисты"
        ordering = ['-time_create']
