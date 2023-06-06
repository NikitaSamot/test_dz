from django import template
from datetime import date
register = template.Library()
from blog.models import MenuItem


@register.filter
def custom_filter(value):
    # Дополнить фильтр согласно вашим требованиям
    return value


@register.filter
def current_year():
    return date.today().year


@register.inclusion_tag('blog/menu.html')
def menu_items():
    items = MenuItem.objects.all()
    return {'menu_items': items}
