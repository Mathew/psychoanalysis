from django.conf.urls import patterns, url


urlpatterns = patterns(
    'psychoanalysis.apps.pa.views',
    url(r'^entry/(?P<reporting_period_id>\d+)/day/(?P<day>\d+)/$', 'day_view',
        name='entry_day'),
    url(r'^entry-list/(?P<reporting_period_id>\d+)/$', 'reporting_period_view',
        name='reporting_period_view'),
)

