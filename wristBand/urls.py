from django.conf.urls import include, url
from django.contrib import admin
from apis.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  url('', include(admin.site.urls)),
  url(r'^test/', wechat_main),
]
