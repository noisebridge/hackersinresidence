from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^opportunities', views.opportunities, name='opportunities'),
    # must be abstracted per opportunity - not just one route
    url(r'^view_opportunity', views.view_opportunity, name='view_opportunity'),
    url(r'^create_opportunity', views.create_opportunity, name='create_opportunity'),
]
