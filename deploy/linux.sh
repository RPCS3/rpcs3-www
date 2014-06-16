#!/bin/bash

# Python
apt-get install python
apt-get install python-dev
apt-get install python-pip

# Modules
pip install django
pip install markdown

# Initialize DB
python ../manage.py syncdb
