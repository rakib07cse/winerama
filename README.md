# winerama
#Backup sqlite3 database and load into mysql database
step 1: Dump database as a json data
python manage.py dumpdata> database.json
or
python manage.py dumpdata --natural-primary --exclude=contenttypes --exclude=auth.Permission --exclude=admin.logentry --exclude=sessions.session --indent 4 > initial_data.json
step 2: Change connection in setting.py 
step 3: Make migrate 
python manage.py migrate
step 4:
python manage.py loaddata initial_data.json
