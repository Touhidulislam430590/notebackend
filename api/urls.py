from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="homeApi"),
    path('notes', views.notesView, name="notes"),
    path('notes/<str:pk>', views.notesView, name="notes"),
]