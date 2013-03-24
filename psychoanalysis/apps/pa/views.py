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

    category_info = period.describe_categories()

    return render(request, 'day_entry_mockup.html', {
        'category_data': simplejson.dumps(category_info),
        'entries': entries,
        'day': day,
    })
