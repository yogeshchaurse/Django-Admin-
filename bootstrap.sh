#!/bin/bash
# Creates the minimal environment needed to start the local installation
# procedure.
# Should only be run on localhost for setting up your local dev environment.
# Assumes an Ubuntu/Debian environment.

# Creates the minimal environment needed to start the local installation
# procedure.
# Should only be run on localhost for setting up your local dev environment.
# Assumes an Ubuntu/Debian environment.

set -e

#sudo apt-get update

# Ensure our system's global pip install is up to date.
wget http://peak.telecommunity.com/dist/ez_setup.py -O /tmp/ez_setup.py
sudo python2.7 /tmp/ez_setup.py -U setuptools
sudo easy_install -U pip
sudo pip2.7 install --upgrade setuptools
sudo pip2.7 install --upgrade distribute
sudo pip2.7 install --upgrade virtualenv

# Create the stub Python virtual environment.

virtualenv -p /usr/bin/python2.7 --no-site-packages .env
echo "Creating Virtual environment for Project"
echo "Enter name for virtual environment" 
read virtual_name
virtualenv $virtual_name
echo "Virtual environment created"

echo "Activating Environment"
cd $virtual_name
. bin/activate

echo "Installing Fabric Deployement tool"
pip install fabric 

echo "Installing pylint for checking coding Standard"
pip install pylint

echo "Install South Migration tool"
pip install south 

echo "Which database you wnat to use 1.Postgresql 2. Mysql"
read choice 

case $choice in
	2) pip install MySQL-Python;;
	1) pip install psycopg2;;
	*) echo "Unknown  Choice";;
esac
pip install Django==1.6
echo "Enter the Django project name"
read project
django-admin.py startproject $project
cd $project 
ls
echo "Please enter the App name you want to create"
read app_name
python manage.py startapp $app_name

python manage.py syncdb

vim fabfile.py

echo "Bootstrap complete!"


