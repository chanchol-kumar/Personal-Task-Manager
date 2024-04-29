from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Task.views import TaskViewSet

router = DefaultRouter() #our Router
router.register(r'task', TaskViewSet,) # Antenna

urlpatterns = [
    path('', include(router.urls)),
]

