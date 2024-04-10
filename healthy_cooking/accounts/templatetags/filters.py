from django import template

register = template.Library()


@register.filter
def placeholder(field, placeholder):

    field.field.widget.attrs['placeholder'] = placeholder
    return field
