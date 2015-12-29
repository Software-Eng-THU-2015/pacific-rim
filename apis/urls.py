from django.conf.urls import include, url
from apis.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'wristBand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'get_plans/', get_plan_history),
    url(r'home/', update_database),
	url(r'tags/post_tag/', insert_tag),
	url(r'tags/(?P<user_id>\w+)/get_tag_list/', get_tag_list),
	url(r'plans/create/', insert_plan),
	url(r'user/(?P<user>\w+)/steps/', get_steps),
    url(r'plans/get_list/', get_plan_list),
    url(r'^tree_main', tree_main),
    url(r'^care_tree', tree_care),
    url(r'^get_tree', get_tree),
    url(r'plans/(?P<plan_id>[0-9]+)/update/', update_plan),
    url(r'^xxoo', test),
]
