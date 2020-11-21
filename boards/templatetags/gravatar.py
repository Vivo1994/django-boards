import hashlib
from  libgravatar import Gravatar
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower()
    default = 'mm'
    size = 256
    g = Gravatar(email)
    url = g.get_image()
    return url