from django.contrib import admin

from models import (
    ReportingPeriod, Category, Activity,
    ActivityEntry, Participant, Profession, User
)

models_tuple = (
    ReportingPeriod, Category, Activity,
    ActivityEntry, Participant, Profession, User
)

for m in models_tuple:
    admin.site.register(m)
