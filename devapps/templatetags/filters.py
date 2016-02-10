from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='clean_unicode')
def clean_unicode(value):
    return value.replace("[","").replace("']","").replace("u'","").replace("'","")