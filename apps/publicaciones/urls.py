from rest_framework.routers import DefaultRouter
from .views import ResolucionViewSet, CategoriasResolucionViewSet, PonenciasViewSet, RevistasTributariaViewSet, MemoriasViewSet, OtrosViewSet

router = DefaultRouter()


router.register(r'resoluciones', ResolucionViewSet, basename='resoluciones')
router.register(r'resoluciones-categorias', CategoriasResolucionViewSet, basename='resoluciones-categorias')
router.register(r'ponencias', PonenciasViewSet, basename='ponencias')
router.register(r'revista-tributaria', RevistasTributariaViewSet, basename='revista-tributaria')
router.register(r'memorias', MemoriasViewSet, basename='memorias')
router.register(r'otros', OtrosViewSet, basename='otros')


urlpatterns = router.urls


