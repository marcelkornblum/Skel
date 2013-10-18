from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'xxxprojectnamexxx.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)




try:
    import sentry
    urlpatterns.append(patterns('',
                       (r'^sentry/', include('sentry.web.urls')),
        ))
except ImportError:
    pass