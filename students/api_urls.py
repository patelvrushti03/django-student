from rest_framework.routers import DefaultRouter
from students.views import StudentModelViewSet

router = DefaultRouter()
router.register("student", StudentModelViewSet)

urlpatterns = router.urls
