import simplejson

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ActivityEntry, ReportingPeriod


@login_required()
def day_view(request, reporting_period_id, day):
    period = ReportingPeriod.objects.get(pk=reporting_period_id)

    entries = period.retrieve_user_entries_by_day(request.user, day)
    category_info = period.describe_categories()

    return render(request, 'day_entry_mockup.html', {
        'category_data': simplejson.dumps(category_info),
        'entries': simplejson.dumps(entries),
        'day': day,
    })
