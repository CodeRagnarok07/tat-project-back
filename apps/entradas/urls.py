from .views import NoticiasListView, NoticiaView, HaciendoDiferenciasListView, HaciendoDiferenciaView, CongresosListView, CongresoView
from rest_framework.routers import DefaultRouter
from django.urls import path, include




urlpatterns = [
    path('noticias/',  NoticiasListView.as_view(), name="noticias"),
    path('noticias/<str:slug>/',  NoticiaView.as_view(), name="view_noticias"),

    path('haciendo-la-diferencia/', HaciendoDiferenciasListView.as_view(), name="haciendo-la-diferencia"),
    path('haciendo-la-diferencia/<str:slug>/', HaciendoDiferenciaView.as_view(), name="view_haciendo-la-diferencia"),

    path('congreso/', CongresosListView.as_view(), name="congreso"),
    path('congreso/<str:slug>/', CongresoView.as_view(), name="view_congreso"),



]