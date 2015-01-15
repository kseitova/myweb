from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import uyghur_web.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uyghur_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^event_form/$', uyghur_web.views.event_form, name='event_form'),
    url(r'^$', uyghur_web.views.index, name='index'),
    url(r'^suggestion/$', uyghur_web.views.suggestion, name='suggestion'),
    url(r'^create_suggestion/$', uyghur_web.views.create_suggestion, name='create_suggestion'),
    #url(r'^admin/', include(admin.site.urls)),

)
