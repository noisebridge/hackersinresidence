#!/bin/bash

# ignore bower and node. if you need to update these,
# just use the command without ignoring these!
python manage.py collectstatic -i node_modules -i bower_components --noinput
