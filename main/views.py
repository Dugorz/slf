from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import *


class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        workers = WorkersModel.objects.all()
        genres = Genre.objects.all()

        context = {'workers': workers, 'genres': genres}
        return render(request, self.template_name, context)


def worker_detail(request, slug):
    worker = get_object_or_404(WorkersModel, slug=slug)

    context = {'worker': worker}
    return render(request, 'main/worker_detail.html', context=context)


def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)

    context = {'genre': genre}
    return render(request, 'main/genre_detail.html', context=context)
