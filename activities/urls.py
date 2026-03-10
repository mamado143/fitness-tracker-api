from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet

# A router automatically generates the standard URLs for our ViewSet
# (e.g., GET /activities/, POST /activities/, GET /activities/{id}/, etc.)
router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
]
