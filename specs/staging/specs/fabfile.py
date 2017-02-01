from fabric.api import local

def dumpdata():
   local('sudo chmod u=rwx /home/mnyman/.virtualenvs/specs/staging/specs/auth/fixtures/auth_data.json ')
   local('sudo chmod g=rw /home/mnyman/.virtualenvs/specs/staging/specs/auth/fixtures/auth_data.json ')
   local('sudo chmod o=rw /home/mnyman/.virtualenvs/specs/staging/specs/auth/fixtures/auth_data.json ')
   local('sudo python manage.py dumpdata --format=json auth > /home/mnyman/.virtualenvs/specs/staging/specs/auth/fixtures/auth_data.json ')
   #local('sudo python manage.py dumpdata --format=json xxxxxxxx > /home/mnyman/.virtualenvs/yyyyyyyy/staging/transdeco/xxxxxxxx/fixtures/xxxxxxxx_data.json ')
   #local('sudo python manage.py dumpdata --format=json xxxxxxxx > /home/mnyman/.virtualenvs/yyyyyyyy/staging/transdeco/xxxxxxxx/fixtures/xxxxxxxx_data.json ')
   #local('sudo python manage.py dumpdata --format=json xxxxxxxx > /home/mnyman/.virtualenvs/yyyyyyyy/staging/transdeco/xxxxxxxx/fixtures/xxxxxxxx_data.json ')
   #local('sudo python manage.py dumpdata --format=json xxxxxxxx > /home/mnyman/.virtualenvs/yyyyyyyy/staging/transdeco/xxxxxxxx/fixtures/xxxxxxxx_data.json ')
   #local('sudo python manage.py dumpdata --format=json xxxxxxxx > /home/mnyman/.virtualenvs/yyyyyyyy/staging/transdeco/xxxxxxxx/fixtures/xxxxxxxx_data.json ')
   #local('sudo python manage.py dumpdata --format=json xxxxxxxx > /home/mnyman/.virtualenvs/yyyyyyyy/staging/transdeco/xxxxxxxx/fixtures/xxxxxxxx_data.json ')
