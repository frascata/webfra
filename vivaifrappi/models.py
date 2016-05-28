import os

try:
    from urllib.parse import urljoin
except ImportError:  # Python 2
    from urlparse import urljoin

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import ImageField
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.managers import SearchableManager
from mezzanine.core.models import Displayable, MetaData, TimeStamped
from mezzanine.galleries.models import BaseGallery, Gallery, GalleryImage
from mezzanine.pages.models import Page, RichTextPage
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
    """
    A page representing the format of the home page
    """
    main_content_title = models.CharField(max_length=100, default=_("Chi Siamo"))
    main_content = models.TextField()
    main_content_class = models.CharField(max_length=100, null=True, blank=True)
    services_page = models.ForeignKey(to="OneSectionPage", null=True, blank=True, default=None)
    portfolio_content_title = models.CharField(max_length=100, default=_(""))
    last_news_visible = models.BooleanField(default=False)
    base_page_template = models.CharField(max_length=100, default="pages/richtextpage.html")

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Home pages")

    def __unicode__(self):
        return '%s - %s' % (self._meta.verbose_name, self.main_content_title)

    def get_absolute_url(self):
        return super(HomePage, self).get_absolute_url()


class Slide(Orderable):
    """
    A slide in a slider connected to a HomePage
    """
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Slide"),
                      upload_to=upload_to("uploads.home.slides", "slider"),
                      format="Image", max_length=255, null=True, blank=True)

    def __unicode__(self):
        return os.path.basename(self.image.name)


class Portfolio(Orderable):
    """
    An icon box on a HomePage
    """
    homepage = models.ForeignKey(HomePage, related_name="portfolios")
    image = FileField(verbose_name=_("Portfolio"),
                      upload_to=upload_to("vivaifrappi.homepage_portfolio", "portfolio"),
                      format="Image", max_length=255)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class OneSectionPage(Page, RichText):
    """
    A page representing the format of the home page
    """
    content_class = models.CharField(max_length=100, null=True, blank=True)
    header_image = ImageField(upload_to=upload_to("uploads.vivaifrappi.one_section_page", "vivaifrappi"),
                              max_length=255)
    extra_gallery = models.ForeignKey(to=Gallery, null=True, blank=True)
    extra_template = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _("One Section Page")
        verbose_name_plural = _("One Section Pages")

    def __unicode__(self):
        return '%s - %s' % (self._meta.verbose_name, self.title)

    def get_absolute_url(self):
        return super(OneSectionPage, self).get_absolute_url()


class ThreeSectionsPage(Page, RichText):
    """
    A page with three content section
    """
    header_image = ImageField(upload_to=upload_to("uploads.vivaifrappi.three_section_pages", "vivaifrappi"),
                              max_length=255)
    content_class = models.CharField(default="default-wrapper", max_length=100, null=True, blank=True)
    content_gallery = models.ForeignKey(to=Gallery, null=True, blank=True, related_name='first_gallery')
    second_content = models.TextField(null=True, blank=True)
    second_content_class = models.CharField(default="light-wrapper", max_length=100, null=True, blank=True)
    second_content_gallery = models.ForeignKey(to=Gallery, null=True, blank=True, related_name='second_gallery')
    third_content = models.TextField(null=True, blank=True)
    third_content_class = models.CharField(default="dark-wrapper", max_length=100, null=True, blank=True)
    third_content_gallery = models.ForeignKey(to=Gallery, null=True, blank=True, related_name='third_gallery')

    class Meta:
        verbose_name = _("Three Sections Page")
        verbose_name_plural = _("Three Sections Pages")

    def __unicode__(self):
        return '%s - %s' % (self._meta.verbose_name, self.title)

    def get_absolute_url(self):
        return super(ThreeSectionsPage, self).get_absolute_url()


class Project(Displayable):
    """
    A model representing a project with gallery
    """
    name = models.CharField(max_length=100)
    members = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=10)
    date = models.DateField(null=True)
    active = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)
    gallery = models.ForeignKey(to=Gallery, null=True, blank=True, default=None)
    page = models.ForeignKey(to=OneSectionPage, null=True, blank=True, default=None)

    objects = SearchableManager()
    search_fields = ("name",)

    def __unicode__(self):
        suffix = u''
        if self.finalized:
            suffix = u"Realizzato"
        return "%s %s" % (self.name, suffix)

    def get_absolute_url(self):
        return self.page.get_absolute_url()
