# About the Infodengue project
<p>

#### *InfoDengue is an alert system for arboviruses based on hybrid data generated through the integrated analysis of data mined from the social Web and climatic and epidemiological data.*
[more](https://info.dengue.mat.br/informacoes/)...
<br/>

## How to contribute?

### Update and install essentials:
```sh
$ sudo apt update && sudo apt -y upgrade
$ sudo apt-get install build-essential git make wget
```

### Install PostgreSQL 12 and PostGIS:
*Download and save datafiles in /Data/docker/demo_data/*
```sh
$ sudo apt update && sudo apt -y upgrade
$ sudo apt-get install build-essential git make wget \
    postgresql-12 postgresql-12-postgis-3 \
    ca-certificates locales --no-install-recommends --yes
```

###  Get Docker:
*https://docs.docker.com/engine/install/ubuntu/*
### Install Docker Compose: 
*https://docs.docker.com/compose/install/*

</p>

### Clone the AlertaDengue repository to your local machine:
```sh
$ git clone https://github.com/AlertaDengue/AlertaDengue.git
```
### Download and restore database from Dataverse:
*Download and save datafiles in /Data/docker/dev_dumps/*
```sh
$ cd Data/
$ make download_demodb
```
[source code](https://info.dengue.mat.br/informacoes/)...

### Configure and deploy AlertaDengue:
```sh
$ make install
$ make sync_mapfiles
$ make run_alertadengue
```

Note:
- *Use the user postgres to configure and restore data in localhost.*

