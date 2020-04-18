from django.urls import path, include
from rest_framework.routers import DefaultRouter

from personal import views

router = DefaultRouter()

router.register(r'goods', views.GoodsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]