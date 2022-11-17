from rest_framework.routers import DefaultRouter
from .views import CompetenciasList, ConveniosViewSet ,AcuerdosViewSet,EdictosViewSet,FlujogramasViewSet,LeyesYDecretosViewSet
router = DefaultRouter()


router.register(r'competencias', CompetenciasList, basename='competencias')
router.register(r'convenios', ConveniosViewSet, basename='convenios')
router.register(r'acuerdos', AcuerdosViewSet, basename='acuerdos')
router.register(r'edictos', EdictosViewSet, basename='edictos')
router.register(r'flujograma', FlujogramasViewSet, basename='competencias')
router.register(r'leyes-y-decretos', LeyesYDecretosViewSet, basename='leyes-y-decretos')


urlpatterns = router.urls