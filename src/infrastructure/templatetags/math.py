from django import template

register = template.Library()


@register.filter
def divide(value, arg):
    """Divide the given value by arg."""

    return str(int(value) // arg)
