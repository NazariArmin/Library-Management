# Library-Management
a jango app that Managing a library for give book to users 



## Setup

### Install python and pip

install python in ubunut:
```bash
  sudo apt-get update && sudo apt-get -y upgrade
  sudo apt-get install python3
```

your python version must be python3 or higher.

you can check it by:
```bash
  python3 -V
```

Install pip in ubuntu:
```bash
  sudo apt-get install -y python3-pip
```


### Install Vertualenv

virtualenv is a virtual environment where you can install software and Python packages in a contained development space.

Install virtualenv in ubuntu:
```bash
  pip3 install virtualenv
```


### Install django

frist you should create a virtualenv

create virtualenv in current directory and call it test:
```bash
  virtualenv test
```

now activate that virtual environment:
```bash
  source test/bin/activate
```

you can see that `test` add befor your device name and username like this:
```bash
  (ENV) username@my-devicename:~$
```

now install django by following cammand:
```bash
  (ENV) username@my-devicename:~$ pip install django
```

and you can see version of your django:
```bash
  (ENV) username@my-devicename:~$ django-admin --version
```




