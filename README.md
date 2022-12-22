# drf-template
 
This is a template for a Django REST Framework project.

`.env` file contains environment variables for the project.

```ruby
POSTGRES_DB=drf_api_template
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
SECRET_KEY=verysecretsomething
```

# Docker Commands
 
- **Build** `Dockerfile` 
  
    `docker build .`

- To **build image** after making changes 

    `docker-compose up --build`
    
- **Start Django Project** using `django` service defined inside docker-compose
  
    `docker-compose run django django-admin startproject intdesk_api .`

- **Start Django App**
  
    `docker-compose run django django-admin startapp users`

- Docker Compose
  
    `docker-compose up`

- **Databse**
  - **Migrate** database 

      `docker-compose run django python manage.py makemigrations`

  - **Apply** migration

      `docker-compose run django python manage.py migrate`

- Crete **superuser** 

    `docker-compose run django python manage.py createsuperuser`

- Install **package**

    `docker-compose run django pip install drf-nested-routers`

# API Endpoints

- **User** endpoints

    - `http://localhost:8000/users/register`
    - `http://localhost:8000/users/login`
    - `http://localhost:8000/users/details`
      - needs `Authorization` header with `Token {{token}}` value 

# Deploy

Update **`settings.py`** file with the following

```python

ALLOWED_HOSTS = ['localhost','127.0.0.1','drf_api.herokuapp.com']

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "deplyed_frontend_url.com"
]

if "DATABASE_URL" in os.environ:
    DATABASES["default"] = env.db("DATABASE_URL")
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

```

update **`requirements.txt`** file with the following

```ruby
uritemplate
gunicorn==20.1.0
whitenoise==5.2.0
django-environ==0.8.1
```

add **`Procfile`** file with the following

```ruby
web: gunicorn drf_api.wsgi --log-file -
```

add **`heroku.yml`** file with the following

```ruby
setup:
  addons:
    - plan: heroku-postgresql
      as: DATABASE
build:
  docker:
    web: Dockerfile
run:
  web: gunicorn drf_api.wsgi:application --bind 0.0.0.0:$PORT
```

add the following CONFIG VARS in Heroku

```ruby
ALLOWED_HOSTS=drf_api.herokuapp.com
DATABASE_URL=postgres://user:pass@host:port/db
SECRET_KEY=verysecretsomething
DISABLE_COLLECTSTATIC=1
HOST=localhost
WEB_CONCURRENCY=1
```