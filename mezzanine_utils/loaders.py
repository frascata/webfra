"""
Wrapper for loading templates from "templates" directories in INSTALLED_APPS
packages.

https://groups.google.com/d/msg/mezzanine-users/XZ1YGLhJp6o/GwmOAey7lncJ
"""

import os
import sys
from importlib import import_module

from django.template import TemplateDoesNotExist
# from django.template.loader import BaseLoader
from django.template.loaders.base import Loader
from django.utils._os import safe_join

from mezzanine.conf import settings
from mezzanine.core.request import current_request

fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()



class MezzanineLoader(Loader):
    is_usable = True

    def __init__(self, engine):
        super(MezzanineLoader, self).__init__(engine)

    def get_template_sources(self, template_name, template_dirs=None):
        """
        Returns the absolute paths to "template_name", within the theme
        specified by SITE_THEME, if the theme is importable.
        """
        theme = settings.SITE_THEME
        if theme:
            request = current_request()
            try:
                mod = import_module(theme)
            except ImportError, e:
                # messages.error(request, 'The theme could not be imported. %s: %s' % (theme, e.args[0]))
                # need to figure out some way to alert admins if a theme is not importable
                pass
            else:
                template_dir = os.path.join(os.path.dirname(mod.__file__), 'templates')
                try:
                    # return safe_join(template_dir.decode(fs_encoding), template_name)
                    return os.path.join(template_dir.decode(fs_encoding), template_name)
                except UnicodeDecodeError:
                    # The template dir name was a bytestring that wasn't valid UTF-8.
                    raise
                except ValueError:
                    # The joined path was located outside of template_dir.
                    pass

    def load_template_source(self, template_name, template_dirs=None):
        filepath = self.get_template_sources(template_name, template_dirs)
        if filepath:
            try:
                file = open(filepath)
                try:
                    return (file.read().decode(settings.FILE_CHARSET), filepath)
                finally:
                    file.close()
            except IOError:
                pass
        raise TemplateDoesNotExist(template_name)


_loader = MezzanineLoader(None)
