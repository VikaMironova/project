from django import template
from myproject.myapp.models import MyModel

register = template.Library()


@register.inclusion_tag('myapp/home.html')
def show_menu():
    menu_items = MyModel.objects.all().values('name', 'slug')
    return {'menu_items': menu_items}
