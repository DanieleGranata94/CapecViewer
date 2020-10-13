from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='str_split')
@stringfilter

def str_split(value, arg):  

    str_split = value.rsplit(' ',3)
#    print(str_split)
	
    return str_split