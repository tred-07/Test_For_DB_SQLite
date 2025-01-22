from django.urls import path,include
from .views import AdvertiseViewsets
from rest_framework import routers
router=routers.DefaultRouter()
router.register('advertise',AdvertiseViewsets)
urlpatterns = [
    path('', include(router.urls))
]