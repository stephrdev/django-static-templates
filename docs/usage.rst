Usage
=====

Configure templates to render
-----------------------------

To configure the templates that should be rendered as static files, add the
``STATIC_TEMPLATES`` setting to your configuration.

.. code-block:: python

    STATIC_TEMPLATES = (
        ('some-template.html', 'rendered.html'),
        ('500.html', 'errors/500.html'),
    )

The setting should be a iterable that returns tuples with to elements.
The tuple's first element is the template path, the second is the path inside
``settings.STATIC_ROOT`` where the rendered content should be stored.


Providing extra context to the templates
----------------------------------------

Remember that the templates are rendered using Django's ``render_to_string``.
If you need extra context when rendering the templates, configure
``STATIC_TEMPLATES_CONTEXT`` as a dictionary.

.. code-block:: python

    STATIC_TEMPLATES_CONTEXT = {
        'DEBUG': False,
        'RAVEN_DSN': 'Some token'
    }


Using a different renderer
--------------------------

If you want to change the way the templates are rendered, you can override the
used renderer by configuring the ``STATIC_TEMPLATES_RENDERER`` setting.

By default, ``static_templates.renderer.Renderer`` is used. Feel free to sub-class
and extend the functionality.


Rendering the templates
-----------------------

To render the templates, use the management command ``render_static_templates``.

.. code-block:: bash

    $ python manage.py render_static_templates
