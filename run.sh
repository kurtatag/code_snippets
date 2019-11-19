#!/bin/bash

gunicorn -b 0.0.0.0:8000 -w 4 wsgi:app
