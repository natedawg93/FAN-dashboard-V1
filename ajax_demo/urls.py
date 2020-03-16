from django.urls import path, include
from django.views.generic.base import TemplateView
from ajax_demo import views
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name="ajax_demo/main.html"), name='room_main'),
    path('rooms/list', views.RoomList.as_view(), name='room_list'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()