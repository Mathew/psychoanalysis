from django.conf.urls import patterns, url


urlpatterns = patterns(
    'psychoanalysis.apps.pa.views',
    url(r'^entry/(?P<reporting_period_id>\d+)/day/(?P<day>\d+)/$', 'day_view',
        name='entry_day'),
)
