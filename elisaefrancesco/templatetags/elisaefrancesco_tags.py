from django import template
from vivaifrappi.models import Project
from webfra import settings

register = template.Library()


@register.simple_tag()
def elisaefrancesco_menu():
    return {
        'menu_items': [
            {
                'label': 'Home',
                'url': '/'
            },
            {
                'label': 'Viaggio di nozze',
                'url': '/honeymoon'
            },
            {
                'label': 'Conferma',
                'url': '/confirm'
            },
            {
                'label': 'Come arrivare',
                'url': '/where'
            }
        ]
    }
