# dalam file urls.py di dalam proyek Django

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from car_dealer.views import DealerViewSet, CarViewSet

router = DefaultRouter()
router.register(r'dealers', DealerViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]