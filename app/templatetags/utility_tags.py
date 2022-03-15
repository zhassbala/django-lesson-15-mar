from django import template

register = template.Library()


@register.filter
def increment(value, number_to_increment):
  return value + number_to_increment
