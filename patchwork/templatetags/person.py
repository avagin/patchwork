# Patchwork - automated patch tracking system
# Copyright (C) 2008 Jeremy Kerr <jk@ozlabs.org>
#
# This file is part of the Patchwork package.
#
# Patchwork is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Patchwork is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Patchwork; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from __future__ import absolute_import

from django.core.urlresolvers import reverse
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from patchwork.filters import SubmitterFilter


register = template.Library()


@register.filter
def personify(person, project):

    if person.name:
        linktext = escape(person.name)
    else:
        linktext = escape(person.email)

    url = reverse('patch_list', kwargs={'project_id': project.linkname})
    str = '<a href="%s?%s=%s">%s</a>' % \
        (url, SubmitterFilter.param, escape(person.id), linktext)

    return mark_safe(str)
