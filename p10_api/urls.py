from django.contrib import admin
from django.urls import path,include
from . import  views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("P10Api",views.P10ApiViewSet,basename="P10Api")

urlpatterns = [
    path("", views.index, name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include(router.urls)),

]
