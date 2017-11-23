from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^opportunities/$', views.opportunities, name='opportunities'),
    # ?P regex extension available in re docs: https://docs.python.org/2/library/re.html
    url(r'^opportunity/(?P<opportunity_id>[0-9]+)/$', views.view_opportunity, name='view_opportunity'),
    url(r'^create/$', views.create_opportunity, name='create_opportunity'),
    url(r'^update_org/$', views.update_organization, name='update_organization'),
    url(r'^lipsum/$', views.lipsum, name='lipsum'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^bugs/$', views.bugs, name='bugs'),
    url(r'^org/$', views.view_organization, name='view_organization'),
]
