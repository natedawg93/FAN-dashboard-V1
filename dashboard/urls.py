from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from rest_framework import routers

from dashboard import views

# router = routers.DefaultRouter()
# router.register(r'users', views.CampusViewSet)
# router.register(r'location', views.LocationViewSet)
# router.register(r'buttons', views.ButtonViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/campus/', views.CampusAPIView.as_view(),name='api-campus'),
    path('api/location/', views.LocationAPIView.as_view(),name='api-location'),
    path('api/button/', views.ButtonAPIView.as_view(),name='api-button'),
    
    path('api/buttonjson/', views.button_list),
    path('api/buttonpost/', views.button_post),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()