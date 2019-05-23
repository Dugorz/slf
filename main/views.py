from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import *


class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        workers = WorkersModel.objects.all()

        context = {'workers': workers}
        return render(request, self.template_name, context)


def worker_detail(request, slug):
    worker = get_object_or_404(WorkersModel, slug=slug)

    context = {'worker': worker}
    return render(request, 'main/worker_detail.html', context)
