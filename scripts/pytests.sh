#!/bin/sh


cd ../src && python3 manage.py test --settings=superapi.settings.developments
