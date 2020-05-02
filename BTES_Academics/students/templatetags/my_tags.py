from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def modulo(num, val):
    return num % val


@register.filter
def update_variable(value):
    data = value
    return data


@register.filter
@stringfilter
def trim(value):
    return value.strip()
