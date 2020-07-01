from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

# Register a new url that points to your custom ViewSet
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]
