from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name='mainview_url'),
    path('worker/<str:slug>/', worker_detail, name='worker_detail_url'),
    path('genre/<str:slug>/', genre_detail, name='genre_detail_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
