
from rest_framework.routers import DefaultRouter

from catalog.views import GroupViewSet, IdolViewSet, PhotocardViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet, basename='group')
router.register('idols', IdolViewSet, basename='idol')
router.register('photocards', PhotocardViewSet, basename='photocard')

urlpatterns = router.urls
