#!/bin/sh

cd ../src && python3 manage.py runserver --settings=superapi.settings.developments
