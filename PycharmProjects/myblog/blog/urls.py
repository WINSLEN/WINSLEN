from django.conf.urls import url,include

from . import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit_action/(?P<article_id>[0-9]+)$', views.edit_action, name='edit_action'),
    url(r'^add_action$', views.add_action, name='add_action'),
    url(r'^add$', views.add_article, name='add_article'),
]
