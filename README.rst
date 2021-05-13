django-static-templates
=======================

.. image:: https://img.shields.io/pypi/v/django-static-templates.svg
   :target: https://pypi.org/project/django-static-templates/
   :alt: Latest Version

.. image:: https://github.com/stephrdev/django-static-templates/workflows/Test/badge.svg?branch=master
   :target: https://github.com/stephrdev/django-static-templates/actions?workflow=Test
   :alt: CI Status

.. image:: https://codecov.io/gh/stephrdev/django-static-templates/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/stephrdev/django-static-templates
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-static-templates/badge/?version=latest
   :target: https://django-static-templates.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status


*django-static-templates* provides a management command to render Django templates
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

A Python 3 interpreter is required in addition to poetry.

.. code-block:: shell

    $ poetry install


Now you're ready to run the tests:

.. code-block:: shell

    $ make tests
