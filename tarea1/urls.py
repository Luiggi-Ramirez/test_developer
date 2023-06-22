from django.urls import path
from tarea1.views import ViewJurisprudencias

urlpatterns = [
    path('<str:search>/', ViewJurisprudencias.as_view())
]
