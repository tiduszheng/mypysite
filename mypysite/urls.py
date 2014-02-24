from django.conf.urls import patterns, include, url
from myBlog import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mypysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^hello/$', views.hello),
    url('^time/$', views.currentDatetime),
    url(r'^time/plus/(\d{1,2})/$', views.timeAhead),
    url(r'^showreq/$', views.showreq),
    url(r'^searchform/$', views.searchform),
    url(r'^admin/', include(admin.site.urls)),
)
