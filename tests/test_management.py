import os
from io import StringIO

from django.core.management import call_command


class TestRenderStaticTemplatesCommand:
    def test_command(self, settings):
        settings.STATIC_TEMPLATES = [('some-template.html', 'rendered/some.html')]
        settings.STATIC_TEMPLATES_CONTEXT = {'EXTRA_FOO': 'bar'}

        out = StringIO()
        call_command('render_static_templates', stdout=out)
        assert out.getvalue().splitlines() == [
            'Rendering static templates..',
            "Processing ('some-template.html', 'rendered/some.html')",
            'Rendering template "some-template.html"',
            'Writing file "{}/rendered/some.html"'.format(settings.STATIC_ROOT),
        ]

        assert 'some.html' in os.listdir(os.path.join(settings.STATIC_ROOT, 'rendered'))
        assert open(
            os.path.join(settings.STATIC_ROOT, 'rendered/some.html')
        ).read().splitlines() == [
            'Lorem Ipsum',
            'Context = bar',
        ]
