# python-desknet

A simple Python wrapper for the DeskNet API.

[![Build Status](https://travis-ci.org/datadesk/python-desknet.png?branch=master)](https://travis-ci.org/datadesk/python-desknet)
[![PyPI version](https://badge.fury.io/py/python-desknet.png)](http://badge.fury.io/py/python-desknet)
[![Coverage Status](https://coveralls.io/repos/datadesk/python-desknet/badge.png?branch=master)](https://coveralls.io/r/datadesk/python-desknet?branch=master)
[![Documentation Status](https://readthedocs.org/projects/django-postgres-copy/badge/?version=latest)](https://django-postgres-copy.californiacivicdata.org/)

* Issues: [github.com/datadesk/python-desknet/issues](https://github.com/datadesk/python-desknet/issues)
* Packaging: [pypi.python.org/pypi/python-desknet](https://pypi.python.org/pypi/python-desknet)
* Testing: [travis-ci.org/datadesk/python-desknet](https://travis-ci.org/datadesk/python-desknet)
* Coverage: [coveralls.io/r/datadesk/python-desknet](https://coveralls.io/r/datadesk/python-desknet)

### Installation

```python
pip install python-desknet
```

## Basic usage

Importing the library

```python
from desknet import DeskNet
```

Creating a new client that can talk to the API

```python
client = DeskNet("your_client_name", "your_client_secret")
```

Create a new element by submitting keyword arguments that correspond [what's supported by DeskNet](http://api.desk-net.com/#api-Element-CreateElement). A dictionary is returned with what was saved to the site, including a unique identifier.

```python
element = client.create(title='This is my budget item')
```
