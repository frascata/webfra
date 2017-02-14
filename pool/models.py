from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

# Create your models here.
from mezzanine.core.models import RichText
from mezzanine.pages.models import RichTextPage, Page


class PoolPage(Page, RichText):
    """
    A page representing a richtext page for Pool site
    """

    class Meta:
        verbose_name = _("Pool Page")
        verbose_name_plural = _("Pool Pages")

    def get_template_name(self):
        return u"pages/poolpage.html"
