from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('psychoanalysis.apps.pa.urls')),
    url(r'^', include('psychoanalysis.apps.pauth.urls')),
    url(r'^padmin/', include('psychoanalysis.apps.padmin.urls')),
    # Examples:
    # url(r'^$', 'psychoanalysis.views.home', name='home'),
    # url(r'^psychoanalysis/', include('psychoanalysis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^day_entry_mockup/$', TemplateView.as_view(template_name='day_entry_mockup.html')),
    url(r'^admin/', include(admin.site.urls)),
)
