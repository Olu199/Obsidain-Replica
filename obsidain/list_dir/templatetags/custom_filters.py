from django import template

register = template.Library()

@register.filter(name='endswith')
def endswith(value, arg):
    """Check if the string ends with the specified argument."""
    if not isinstance(value, str):
        return False
    return value.lower().endswith(arg.lower())
