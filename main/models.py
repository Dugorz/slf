from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse, redirect
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class WorkersModel(models.Model):
    worker_name = models.CharField(max_length=50, verbose_name='Имя сотрудника')
    worker_photo = models.ImageField(upload_to='media', verbose_name='Портрет сотрудника')
    worker_portfolio = models.ManyToManyField('Image', related_name='images')
    genre = models.ManyToManyField('Genre', related_name='genres')
    slug = models.SlugField(max_length=50)
    description = models.CharField(max_length=4000, verbose_name='Информация о сотруднике')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('worker_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.worker_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.worker_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Жанр')
    cover = models.ImageField(verbose_name='Обложка', max_length=250)
    photo_examples = models.ManyToManyField('Image', verbose_name='examples')
    slug = models.SlugField(max_length=50, db_index=True)

    def get_absolute_url(self):
        return reverse('genre_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Image(models.Model):
    name = models.CharField(max_length=150, verbose_name='Идентификатор изображения')
    image = models.ImageField(upload_to='media', verbose_name='Изображение')
    slug = models.SlugField(max_length=50)

    # def get_absolute_url(self):
    #     return reverse('image_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
