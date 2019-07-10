This is a small `hello_world` Django application containing a Postgres database, Celery & Redis.
Its sole purpose is to compare different cloud providers, CI/CD tools and repositories to assess 
costs and find the best choices for it. 

### Setup
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate

You also need to make an env.yml file that contains the environment variables required for the application, 
I suggest asking one of your peers for a copy of this, as its kept out of version control. Depending on the 
cloud provider, we will need it in Production or not.

### Running
    ./manage.py runserver

### Testing
    fab test

### Deployment

#### - Heroku

Heroku CD will push the changes directly.

http://curiosity-wab.herokuapp.com
