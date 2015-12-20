from django.conf.urls import include, url
from apis.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'get_plans/', get_plan_history),
	url(r'tags/post_tag/', insert_tag),
]
