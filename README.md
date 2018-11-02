# Bicycle Project

This project is a TEST, not production execute please

# Install

for install create a environment and execute pip install -r requiriments.txt
create file database_info
* ENGINE= ENGINE
* PORT = PORT
* HOST = HOST
* USER = USER
* PASSWORD = PASSWORD
* NAME = DBNAME

# Methods

* GET
    * /bicycle/list (List all registers for biclycles)

* POST
    * /bicycle/list (Add new bicycle, send JSON post with brand and serial params)

* UPDATE (Patch, PUT)
    * /biclycle/update/<id> (Update bicycle send JSON with params)

* DELETE
    * /biclycle/delete/<id> (Delete bicycle for id)
    

# TEST

Run tests with python manage.py test --settings=merlin.settings.settings_development


# app.yaml

This file contains configuration information for deployment to App Engine.