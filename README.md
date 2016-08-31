# discosub 0.1.7

Simple and faster subdomain discover

* Free software: GNU General Public License v3

## install
### From pypi
```shell
pip install discosub
```

### As a docker container
```shell
docker pull 4383/discosub:latest
```

### from sources
```shell
$ git clone https://github.com/4383/discosub
$ cd discosub
$ python setup.py install
```

## Usages
### From pypi
```shell
discosub run <your target domain>
```

### Inside a docker container
```shell
docker run -e "TARGET=<your target domain>" 4383/discosub:latest
```

### from sources
```shell
$ discosub run <your target domain>
```

## Prerequistes
* python >= 2.7 (but prefer python3.x)

## Features
* Analyze a root domain a discover these subdomains

## Guidelines
* Distributing via pipy
* Using system command (```$ discosub run <your target domain``` instead of ```$ python discosub/main.py run <your target domain>```)
* Execute discosub in a docker container and provide a standalone image of this

## Credits
Author: 4383 (Hervé Beraud)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
