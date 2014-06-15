#!/bin/bash

# Python
apt-get install python
apt-get install python-dev
apt-get install python-pip

# Django
pip install django

# Initialize DB
python ../manage.py syncdb
