from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse, redirect
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class WorkersModel(models.Model):
    worker_name = models.CharField(max_length=50, verbose_name='Worker name')
    worker_photo = models.ImageField(upload_to='media', verbose_name='Worker portrait', blank=True)
    slug = models.SlugField(max_length=50)
    worker_portfolio = models.ImageField(verbose_name='Worker portfolio', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('worker_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.worker_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.worker_name

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
