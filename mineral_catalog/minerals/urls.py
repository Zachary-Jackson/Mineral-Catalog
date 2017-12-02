from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'mineral/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'', views.detail_home, name='detail_home')

]
