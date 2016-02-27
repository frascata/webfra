from django.utils.translation import ugettext
from django import template
from django.core.serializers.json import DjangoJSONEncoder
from vivaifrappi.models import Project
from webfra import settings

register = template.Library()


@register.filter
def jsonify(obj, value=None):
    import json

    return json.dumps(obj, cls=DjangoJSONEncoder)


@register.inclusion_tag('includes/projects.html')
def show_projects(finalized=False):
    return {
        'projects': Project.objects.filter(finalized=finalized, active=True).order_by('-date'),
        'MEDIA_URL': settings.MEDIA_URL
    }
