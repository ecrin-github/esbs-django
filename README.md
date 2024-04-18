# ECRIN Systems Back-end Services (ESBS)

- [ESBS](#ecrin-systems-back-end-services--esbs-)
    - [Description](#description)
    - [Project structures](#project-structures)
    - [Application structures](#application-structures)
    - [Tools and frameworks](#tools-and-frameworks)
    - [Launching](#launching)
    - [Authentication and Permissions](#authentication-and-permissions)
    - [API](#api)
    - [Changelog](CHANGELOG.md)


## Description
**ECRIN Systems Back-end Services (ESBS)** is the set of back-end services, which provides the core functionality for 
ECRIN needs both for the front-end development and integration with other services.

It includes the following subsystems (services):
- User's management service (integrated with the [LifeScience AAI](https://lifescience-ri.eu/home.html));
- Repository Management service (The RMS portal related endpoints);
- MetaData Repository service (The MDR portal related endpoints), including:
  - The MDR search API (in development);
  - The MDR integration scripts.
- Context data management service;
- General data management service.

## Project structure
The ESBS project's root folder contains the following directories and files:
- `configs` (hidden; included in `.gitignore`) - includes all necessary configurations, which should be secured;
- `context` - contains the **Context data management service** source code;
- `db_exports` - contains Database backup files (in development);
- `deploy` - includes the `docker-compose.yml` file to run the ESBS services in `Docker` containers;
- `esbs` - includes the core project's settings, urls, etc.;
- `general` - contains the **General data management service** source code;
- `mdm` - contains the **MDR related service** source code;
- `rms` - contains the **RMS related service** source code;
- `users` - contains the **Users management service** source code;
- `templates` - contains custom `HTML` templates;
- `.dockerignore` - Docker ignore file (lists the files, excluded from the `Docker` container)
- `.gitignore` - includes files and folders to be ignored while committing to `Git`;
- `CHANGELOG.md` - list all changes;
- `db.sqlite3` - `SQLite` database file for local development needs;
- `Dockerfile` - `Docker` container file;
- `manage.py` - contains all necessary `Django` commands;
- `README.md` - contains the **ESBS** project details;
- `requirements.txt` - contains all needed dependencies to be installed to run the project.


## Application structures
Each service has the following structure:
- `migrations` - contains database migrations;
- `models` - contains all service's entities (DB tables);
- `serializers` - contains `DTO` (Data Transfer Objects) of the service. There are two main types of serializer's objects:
  - `*InputSerializer` classes - are used when someone wants to make `POST`, `PUT`, `PATCH` requests;
  - `*OutputSerializer` classes - are used when someone wants to retrieve data from the service (`GET` requests).
- `views` - contains `Controllers`;
- `__init__.py` - is used to make the directory as Python package;
- `admin.py` - determines which models will be available in the [Django Admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/) interface;
- `apps.py` - service application files;
- `tests.py` - includes relevant `unit` tests;
- `urls.py` - contains all service's routers.


## Tools and frameworks
- Python (v. 3.11);
- [Django Framework (v. 4.11)](https://docs.djangoproject.com/en/4.1/);
- [Django REST Framework](https://www.django-rest-framework.org/);
- [DRF Yasg](https://drf-yasg.readthedocs.io/en/stable/);
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/);
- [Mozilla Django OIDC](https://github.com/mozilla/mozilla-django-oidc).


## Launching
To launch the project on our local machine, you can use the following command:<br />
```
> python manage.py runserver 7220
```
Also, you can use the `Docker compose` command:
```
> cd deploy
> docker compose up
```

## Authentication and Permissions
To implement all necessary **Authorization and Authentication** needs the `Mozilla Django OIDC` library and integrated [Django Authentication Backend](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#authentication-backends) are used. 
To use the `OIDC` functionality, the `LifeScience AAI` service has been used.

In addition, all endpoints were extended with `authentication_classes` attribute, which idea is to specify user's authentication 
ways to be used to access specific endpoint(s).<br />
There are four main authentication classes used to protect the API:
- `SessionAuthentication` - session-based authentication;
- `BasicAuthentication` - basic authentication type, which uses `username` and `password` to authorise user;
- `TokenAuthentication` - token-based authentication;
- `OIDCAuthentication` - OIDC-based authentication, which connects authentication class from the `Mozilla Django OIDC` library.

To manage accesses to any specific endpoint, you can modify the following configuration, which can be found in any
`views.py` file:
```
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```
There are various options for permissions, like:
- `IsAuthenticatedOrReadOnly` - if the user is authenticated in the system, he can modify the specific `Model`, otherwise - just read (view) it;
- `IsAuthenticated` - the user can read and modify the specific `Model` only if he is authenticated in the system (no anonymous access at all);
- `IsAdminUser` - the user must be an `admin` to be able to read and modify the specific `Model`.

## API
All services' endpoints are listed on the `Swagger` and `Redoc` pages, available on:
- `http://host:port/swagger` (Swagger UI);
- `http://host:port/redoc` (Redoc UI).