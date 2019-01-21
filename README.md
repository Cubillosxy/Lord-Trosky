# Lord-Trosky
Blog with Django, React and API Rest for mobile APP's


## Build

    docker-compose build

## Running

    docker-compose up
    
## Database

dump:

    docker exec lord-trosky_db_1 bash -c 'pg_dump --dbname=postgres --username=postgres > /tmp/data/db.dump'

restore:

    docker exec lord-trosky_db_1 bash -c 'psql --dbname=postgres --username=postgres --command="DROP SCHEMA public CASCADE;CREATE SCHEMA public;" && pg_restore /tmp/data/db.dump --dbname=postgres --username=postgres --no-owner'

You can connect to the database shell using:

    docker exec -it lord-trosky_db_1 psql --dbname=postgres --username=postgres

## Commands


To run any other command on the app container:

    docker exec -it lord-trosky_web_1 python manage.py createsuperuser
    docker exec -it lord-trosky_web_1 python manage.py shell_plus
    docker exec -it lord-trosky_web_1 python manage.py test --failfast --parallel
    docker exec -it lord-trosky_web_1 bash


## Enable local email

in settings.py:

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'