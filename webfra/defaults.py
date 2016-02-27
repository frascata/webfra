from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting

THEME_CHOICES = (
    ('', _("Default")),
    ('vivaifrappi', _("Vivai frappi")),
    ('test_fra', _("Test Fra")),
)

register_setting(
    name="SITE_THEME",
    label=_("Theme"),
    description=_("The theme to use with the site."),
    editable=True,
    choices=THEME_CHOICES,
    default='',
)