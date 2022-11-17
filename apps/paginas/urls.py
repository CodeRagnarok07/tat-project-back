from django.urls import path, include
from .views import PaginasListView, PaginaView

urlpatterns = [
    path('',  PaginasListView.as_view(), name="paginas"),
    path('<int:page>',  PaginaView.as_view(), name="paginas"),

]