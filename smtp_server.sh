#!/bin/bash

# From: http://stackoverflow.com/questions/5802189/django-errno-111-connection-refused
# There is a django alternative listed in this answer that may be
# better in the long term. We should explore that too. (Django: console.EmailBackend)
python -m smtpd -n -c DebuggingServer localhost:1025
