from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

THEME_CHOICES = (
    ('', _("Default")),
)

register_setting(
    name="SITE_THEME",
    label=_("Theme"),
    description=_("The theme to use with the site."),
    editable=True,
    choices=THEME_CHOICES,
    default='',
)
