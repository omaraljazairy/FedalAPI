# Fedal API
### Table of Contents
#### [Description](#description)
#### [Built with](#built-with)
#### [Install](#install)
#### [Usage](#usage)
#### [Changelog](#changelog)
#### [Bugs](#bugs)
#### [Contributing](#contributing)
#### [Authors](#authors)
#### [License](#license)

## Description
A Django Backend API used for my own projects. The API will used for front-end websites, mobile apps and command line applications. The API runs inside a docker container. For local testing, it uses a MySQL image connected to it. There is a PHPMyAdmin connected to the MySQL database.

## Built with
This API is built in Python3.8 using the Django 3 and the Django Restframework 3.

## Install
The API requires docker and docker-compose to be installed. After installing them, create the file .env and add the following environment variables:
> DB_USER=root
> DB_PASSWORD=dockerpass
> DB_HOST=174.27.0.2
> DB_PORT=3306
> DB_DATABASE=API
> ENVIRONMENT=pro
> LEVEL=INFO
> SECRET_KEY=your-django-secret-key
> DEBUG=0

The values of these variable can be modified. Some variables are used in the docker-compos.yml and others will be used in the API its self.

After creating the .env file, the project can be cloned. Enter the project folder and run the following commands:
```sh
docker-compose build
docker-compose up -d
```
  
## Usage
After installing the required packages and running docker-compose, the API will be accessed internally by the browser with the following ipaddress: 0.0.0.0:8002/admin.
To access the API and the MySQL containers, first run the command
```sh
docker ps
```
from the command line. this will give you the name of the container and the port.
Assuming the container name of the API is fedalapi-django, you can access it and create an admin user using the following commands from the command line
```sh
docker exec -it fedalapi-django bash
python manage.py createsuperuser --email admin@example.com --username admin
```
After creating the admin user, the admin page can be accessed by the created admin user.
The Database will also be access either by using the command line and accessing the container or using
PHPMyAdmin that can be accessed internally by the browser with the following ipaddress: 0.0.0.0:8082.

The .env file will create the environment variables that will be used in the docker-compose.yml and the application.

## Changelogs
All change logs can be found [here](CHANGELOG.md)

## Bugs

## Authors
Omar Aljazairy omar@fedal.nl

## License
This projects used the [MIT license](LICENSE)