from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^suggestion/$', hello.views.suggestion, name='suggestion'),
    url(r'^create_suggestion/$', hello.views.create_suggestion, name='create_suggestion'),
    #url(r'^admin/', include(admin.site.urls)),

)
