from django import template

register = template.Library()


@register.filter
def custom_filter(value):
    # Дополнить фильтр согласно вашим требованиям
    return value
