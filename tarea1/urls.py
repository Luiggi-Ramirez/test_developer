from django.urls import path
from tarea1.views import ViewJurisprudencias

urlpatterns = [
    path('', ViewJurisprudencias.as_view())
]
