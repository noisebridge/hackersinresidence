"""hackersinresidence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# for redirects
from django.views.generic import RedirectView

# for static media in dev
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('webapp.urls')),
    # only exposed on root path now
    #url(r'^webapp/', include('webapp.urls')),
    url(r'^admin/', admin.site.urls),
    # is this the best way to override admin.site.urls?
    # /admin/ when logged out should probably redirect to /admin/login/
    url(r'^admin/login$', RedirectView.as_view(pattern_name='admin-login', permanent=True)),
    # when you sign up, the post fails... is this complete? check pinax docs
    url(r'^account/', include('account.urls')),
    # for static media in dev
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
