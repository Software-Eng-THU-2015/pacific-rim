from django.conf.urls import include, url
from django.contrib import admin
import apis.views
from apis.views import index
# from apis import views
from apis import server
# from apis import models


urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^apis/', include('apis.urls')),
    url(r'^$', index),
    url(r'^test/', server.handle),
     url(r'^tag', apis.views.tag_test),
]
