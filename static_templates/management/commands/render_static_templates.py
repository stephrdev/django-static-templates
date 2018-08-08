from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import translation

from ...renderer import get_renderer


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Acrtivate language to ensure we get the translation right.
        translation.activate(settings.LANGUAGE_CODE)

        self.stdout.write('Rendering static templates..')

        renderer = get_renderer()

        templates = getattr(settings, 'STATIC_TEMPLATES', {})

        for configuration in templates:
            renderer(configuration, stdout=self.stdout).render()
