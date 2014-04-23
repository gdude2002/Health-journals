Health-journals
===============

A simple Bottle app for keeping track of eating, exercise and sleeping habits on a daily basis. Designed with groups in mind.

### Requirements

* Python 2.7
* Beaker
* Bottle
* CherryPy
* [PyMongo](http://api.mongodb.org/python/current/tutorial.html)

### Setting up

* `pip install -r requirements.txt`
* If you need to, copy `development.yml.example` to `development.yml` in the `config/` directory and edit it.
* For development:
  * `python run.py`
* For production:
  * Do yourself a favour and use `uWSGI`.
