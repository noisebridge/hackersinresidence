from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^opportunities', views.opportunities, name='opportunities'),
    # ?P regex extension available in re docs: https://docs.python.org/2/library/re.html
    url(r'^opportunity/(?P<opportunity_id>[0-9]+)/$', views.view_opportunity, name='view_opportunity'),
    url(r'^create_opportunity', views.create_opportunity, name='create_opportunity'),
]
