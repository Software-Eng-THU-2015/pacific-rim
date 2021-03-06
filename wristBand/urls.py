from django.conf.urls import include, url
from django.contrib import admin
import apis.views
from apis import server
# from apis import models
import apis.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^apis/', include(apis.urls)),
    url(r'^tag_main', apis.views.tag_main),
    url(r'^update', apis.views.update_database),
    # url(r'^tag', apis.views.tag_test),
]
