#!/bin/sh
./manage.py dumpdata --indent=4 acls agencies permissions projects telecomm tools workflows auth sites > backup_data.json

