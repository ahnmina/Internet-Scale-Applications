from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.current_datetime, name='datetime'),
    url(r'^$', views.homepage, name='homepage'),
]