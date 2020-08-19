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

After running the project in the first time, it is necessary to populate the database with some necessary data (while the container is up).

To do that, run the script:

```sh
./scripts/build_dev.sh
```

### 🏠 Local settings

A templete for the server local_settings is provided under the name ```local_settings.docker.py```. Create a copy of this file with the name ```local_settings.py``` inside the **thundersite** folder. It is not necessary to change anything to run the docker image, change the configurations as needed in development enviroment

### 🍱 Assets

To download all site images, run the following commands

```sh
cd wget
./dump.sh
```

All files of type jpg, png or gif from the site will be downloaded inside a folder named **thunderatz.org**. The ```local_settings.docker.py``` points to that folder to find static and media files.
