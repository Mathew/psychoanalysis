from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    'psychoanalysis.apps.padmin.views',
    url(r'^$', TemplateView.as_view(template_name="padmin/admin_index.html"),
        name="admin_index"),
    url(r'^chart/(?P<data>\d+)/(?P<chart_type>.+)/$', 'chart_view',
        name='chart_view'),
)
