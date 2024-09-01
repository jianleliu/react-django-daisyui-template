# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyAppViewSet

router = DefaultRouter()
router.register(r'myapp', MyAppViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
