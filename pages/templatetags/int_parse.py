from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='int_parse')
@stringfilter

def int_parse(value, arg):  

    split = value.rsplit(' ',3)
#    print(split)
    return split