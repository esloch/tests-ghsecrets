# About the Infodengue project
<p>

*InfoDengue: a nowcasting system for the surveillance of dengue fever transmission.*
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
### Clone the data repository and restore the database:
*The data is randomly inserted into the database for testing and development of the AlertDengue project.*
[source code](https://github.com/AlertaDengue/Data/blob/master/README.md)...

### Configure and deploy AlertaDengue:
```sh
$ cd
$ make install
$ make sync_mapfiles
$ make run_alertadengue
```
