from rest_framework.routers import DefaultRouter

from catalog.views import GroupViewSet, IdolViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet, basename='group')
router.register('idols', IdolViewSet, basename='idol')

urlpatterns = router.urls
