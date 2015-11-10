from django.conf.urls import include, url
from django.contrib import admin
from apis import views
from apis import server


urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  url('', include(admin.site.urls)),
  url(r'^test/', server.handle),
]
