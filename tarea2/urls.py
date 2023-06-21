from django.urls import path
from tarea2.views import ViewConcesiones

urlpatterns = [
    path('', ViewConcesiones.as_view()),
]
