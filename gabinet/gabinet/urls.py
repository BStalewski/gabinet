from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gabinet.views.home', name='home'),
    # url(r'^gabinet/', include('gabinet.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(pages.urls)),
)
