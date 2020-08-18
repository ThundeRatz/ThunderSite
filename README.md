# ⚡ ThunderSite

Developed with Django 2.0

To start the Django development server along with postgres database, use the command

```sh
docker-compose up
```

## 🎈 First setup

### 🐋 Docker

To start the docker development enviroment, it is necessary to install ```docker``` and ```docker-compose```

Check the guide for [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/)

Once ```docker``` is available, you can build the enviroment with the following command inside the project's folder

```sh
docker-compose build
```

Before running the project in the first time, it is necessary to populate the database with some necessary data.

To do that, run the command:

```sh
TODO: seeds script
```

### 🏠 Local settings

A templete for the server local_settings is provided under the name ```local_settings.docker.py```. Create a copy of this file with the name ```local_settings.py``` inside the **thundersite** folder. It is not necessary to change anything to run the docker image, change the configurations as needed in development enviroment
