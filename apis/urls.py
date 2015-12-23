from django.conf.urls import include, url
from apis.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'get_plans/', get_plan_history),
	url(r'tags/post_tag/', insert_tag),
	url(r'plans/create/', insert_plan),
    url(r'plans/get_today/', get_plan_list),
    url(r'^tree_main', tree_main),
    url(r'^care_tree', tree_care),
    url(r'^get_tree', get_tree),
]
