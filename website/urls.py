from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',

    url(r"^$", views.EditionListView.as_view() , name="list"),
    url(r"^(?P<slug>[\w-]+)/$", views.ArticleListView.as_view(), name="detail"),

)