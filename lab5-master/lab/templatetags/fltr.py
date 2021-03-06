from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter

def cut(value, arg):
    return value.replace(arg, '')