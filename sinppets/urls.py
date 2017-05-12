# Author:xubojoy
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sinppets import views

#--------------函数视图urls----------------------------------
# urlpatterns = [
#     url(r'^snippets/$',views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail),
# ]


#--------------------使用类视图重构视图、mixins、通用类视图书写URLs--------------------------------

urlpatterns = [
    url(r'^snippets/$',views.SnippetList.as_view()),
    url(r'^snippets/(?P<id>[0-9]+)/$',views.SnippetDetail.as_view()),
    url(r'^user/$',views.UserList.as_view()),
    url(r'^user/(?P<id>[0-9]+)/$',views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)