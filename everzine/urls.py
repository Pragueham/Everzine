from django.conf.urls import patterns, include, url
from django.conf import settings
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'everzine.views.home', name='home'),
    # url(r'^everzine/', include('everzine.foo.urls')),
    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r"^articles/", include("website.urls", namespace="articles")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
