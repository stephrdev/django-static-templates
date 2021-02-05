import importlib
import os

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.signed_cookies import SessionStore
from django.template import RequestContext
from django.template.loader import render_to_string
from django.test.client import RequestFactory


class Renderer(object):
    """
    Renderer is used to convert a template into a static file.
    """

    configuration = None
    stdout = None

    def __init__(self, configuration, stdout=None):
        """
        The init function takes a row from settings.STATIC_TEMPLATES.
        By default, the users are required to provide a two-item tuple with the
        template name and the static file path.
        """
        assert len(configuration) == 2
        self.configuration = configuration
        self.stdout = stdout

    def log(self, message):
        if self.stdout:
            self.stdout.write(message)

    def render(self):
        """
        render starts the rendering process for the given configuration.
        """
        self.log('Processing {0}'.format(self.configuration))
        content = self.render_template()
        self.write_static_file(content)

    def get_template_name(self):
        """
        Returns the template name to use when rendering to static.
        """
        return self.configuration[0]

    def get_template_context(self):
        """
        Provides the context for render_template call.
        """
        return getattr(settings, 'STATIC_TEMPLATES_CONTEXT', {})

    def render_template(self):
        """
        Creates a fake request context together with the context from
        ``get_template_context`` and returns the rendered output.
        """

        # We need a fake request to use the RequestContext, which is needed to
        # apply all context processors (for menus, etc.)
        request = RequestFactory(HTTP_HOST=settings.ALLOWED_HOSTS[0].strip('.')).get('/')
        request.user = AnonymousUser()
        request.session = SessionStore()

        template_name = self.get_template_name()
        self.log('Rendering template "{0}"'.format(template_name))
        return render_to_string(
            template_name,
            context=RequestContext(request, self.get_template_context()).flatten(),
            request=request,
        )

    def get_static_file_path(self):
        """
        Returns the target static file path to store the content to.
        """
        return self.configuration[1]

    def write_static_file(self, content):
        """
        write_static_file makes sure that the target directory exists and writes
        the provided content to a file.
        """
        path = os.path.join(settings.STATIC_ROOT, self.get_static_file_path())
        directory = os.path.dirname(path)
        if not os.path.isdir(directory):
            os.makedirs(directory)

        self.log('Writing file "{0}"'.format(path))
        with open(path, 'w+') as file_obj:
            file_obj.write(content)


def get_renderer(path=None):
    """
    Load a renderer and return the class. If a path is provided, the renderer is
    imported from that path. By default, ``static_templates.renderer.Renderer``
    is used.
    """
    path = path or getattr(
        settings,
        'STATIC_TEMPLATES_RENDERER',
        'static_templates.renderer.Renderer'
    )

    module_name, class_name = path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    renderer_class = getattr(module, class_name)
    return renderer_class
