from django import template

register = template.Library()

@register.filter
def dictlookup(obj, key):
    return getattr(obj, key, "")
