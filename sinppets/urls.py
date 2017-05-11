# Author:xubojoy
from django.conf.urls import url
from sinppets import views

urlpatterns = [
    url(r'^snippets/$',views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail),
]