from django import template

register = template.Library()

@register.filter
def add_class(value, css_class):
    css_classes = value.field.widget.attrs.get('class', '')
    css_classes += f' {css_class}'
    value.field.widget.attrs['class'] = css_classes.strip()
    return value
