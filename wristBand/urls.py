from django.conf.urls import include, url
from django.contrib import admin
from apis.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^apis/', include('apis.urls')),
    url(r'^$', index),
]
