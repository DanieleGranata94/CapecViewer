from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='parse')
@stringfilter

def parse(value, arg):

    list = []
    split = value.split("::")
    
    for s in split:
        if s=='':
            pass
        else:
            rep1 = s.replace(':', ' ')
            rep2 = rep1.replace('NATURE','')
            list.append(rep2)

    return list