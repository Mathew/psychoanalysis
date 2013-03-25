psychoanalysis
==============

NHS Hack Day project.

A quick hack project over the weekend for assigning various job roles different types
of activities to be tracked.  These can then have reports ran on them, compared to different time periods and used to improve workflow/identify issues with practitioners.

Commands
------

python manage.py runserver 0.0.0.0:8000 --settings=psychoanalysis.settings.development

TODO:
----

* Fix posting for activity entries.
* Remove ugo javascript
* Fix inserts so they only need to occur when an item is created (instead of that honking great database for loop)
* Style/Fix HTML.
* Create a better user display for inputting activity entries.
* At the very least split categories/activities into their own select boxes and filter the activities dependant on the category selected.
* Move charting into its own app.
* Improve Backbone so we aren't creating json strings, forms and triggering button clicks.
* Try to move the majority of the setup/creation out of the Django admin for a smoother, simplified experience.
* Make sure MC Nickle doesn't drink again.
* Look at database schema again.
* Add tests!
