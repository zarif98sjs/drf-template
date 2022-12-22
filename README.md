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

