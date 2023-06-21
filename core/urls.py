from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("jurisprudencias/", include('tarea1.urls')),
    path("scraping/", include('tarea2.urls')),
]
