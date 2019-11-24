# Tutorial: CRUD with Pyramid, Pymongo and WTForms
==================

## About
---------------
This repository contains the code written along the tutorial series "Tutorial 1" about Pyramid that can be found at the link below:
- <https://blog.albertosenna.com/pyramid/>

The goal is to keep track of what I have been studying about Pyramid.
At each branch you can find the code developed during a certain step of the process.

## Getting Started
---------------
To run the final product do the following:
Create a database according to the second part of the tutorial:
- <https://blog.albertosenna.com/2019/11/24/pyramid-02-mongodb-setup/>

Clone this repository:
```
git clone https://github.com/albertosdneto/tutorial_pyramid_mongo.git

cd tutorial_pyramid_mongo/
```

Create a virtual environment and update it:
```
python3 -m venv env

env/bin/pip install --upgrade pip setuptools
```
Install the application:
```
env/bin/pip install -e .
```
Run the application:
```
env/bin/pserve development.ini --reload
```

I hope you enjoy.