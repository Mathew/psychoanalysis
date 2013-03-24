import datetime
import simplejson

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ActivityEntry, ReportingPeriod


@login_required()
def day_view(request, reporting_period_id, day):
    period = ReportingPeriod.objects.get(pk=reporting_period_id)

    # hack for javascript to have an ID associated with a slot.
    period.create_user_day_entries(request.user, day)

    entries = period.retrieve_user_entries_by_day(request.user, day)
    entries = simplejson.dumps([e.to_dict() for e in entries])

    if request.POST:
        for k, v in simplejson.loads(request.POST['data']):
            ae = ActivityEntry.objects.get(pk=k)
            ae.activity_pk = v
            ae.save()

    category_info = period.describe_categories()

    return render(request, 'day_entry_mockup.html', {
        'category_data': simplejson.dumps(category_info),
        'entries': entries,
        'day': day,
    })


def create_date_info(base, x, reporting_period_id):
    return {
        'date': (base - datetime.timedelta(days=x)).strftime("%A %d/%m/%y"),
        'reporting_period_id': reporting_period_id,
        'day': x
    }


@login_required()
def reporting_period_view(request, reporting_period_id):
    period = ReportingPeriod.objects.get(pk=reporting_period_id)
    data = []

    diff = period.end_date - period.start_date
    for x in xrange(1, diff.days + 1):
        data.append(create_date_info(period.start_date, x, reporting_period_id))

    return render(request, 'pa/reporting_period_view.html', {
        'dates': data
    })
