#!/bin/bash

while true;
    do git fetch --all;
    git rebase origin/master;
    git push heroku master -f;
    heroku run "python ./manage.py syncdb --settings=psychoanalysis.settings.production";
    heroku run "python ./manage.py migrate --settings=psychoanalysis.settings.production";
    sleep 60;
done;