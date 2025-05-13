from rest_framework.routers import DefaultRouter
from .views import DailyUsageViewSet

router = DefaultRouter()
router.register(r'', DailyUsageViewSet, basename='usage')

urlpatterns = router.urls
