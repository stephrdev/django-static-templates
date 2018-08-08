django-static-templates
=======================

.. image:: https://img.shields.io/pypi/v/django-static-templates.svg
   :target: https://pypi.org/project/django-static-templates/
   :alt: Latest Version

.. image:: https://codecov.io/gh/moccu/django-static-templates/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/moccu/django-static-templates
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-static-templates/badge/?version=latest
   :target: https://django-static-templates.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/moccu/django-static-templates.svg?branch=master
   :target: https://travis-ci.org/moccu/django-static-templates


*django-static-templates* provides a management command to render Django templats
as static files. Example usage might be static error pages to delivered by your reverse proxy
if the Django applications dies.


Features
--------

* Management command ``render_static_templates`` to create static files in your STATIC_ROOT.
* Helpers to render templates as static files


Requirements
------------

django-static-templates supports Python 3 only and requires at least Django 1.11.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
---------

* `Documentation <https://django-static-templates.readthedocs.org/>`_
* `Bug Tracker <https://github.com/moccu/django-static-templates/issues>`_
* `Code <https://github.com/moccu/django-static-templates/>`_
