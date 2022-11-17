from .views import DepartamentoViewSet, OficinaViewSet, AutoridadViewSet, EquipoViewSet, AutoridadDetail, EquipoDetail
from rest_framework.routers import DefaultRouter
from django.urls import path, include



# autoridad_list = AutoridadViewSet.as_view({'get': 'list'})
# autoridad_detail = AutoridadViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register(r'oficinas', OficinaViewSet, basename='oficinas')
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'autoridades', AutoridadViewSet, basename='autoridades')
router.register(r'equipo', EquipoViewSet, basename='equipo')


urlpatterns = [
    path('', include(router.urls)),
    path('autoridades/<str:slug>/',  AutoridadDetail.as_view(), name="AutoridadDetail"),
    path('equipo/<str:slug>/',  EquipoDetail.as_view(), name="EquipoDetail"),
]


