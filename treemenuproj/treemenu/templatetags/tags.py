from pathlib import Path
from typing import Optional

from django import template
from django.template import RequestContext

from treemenu.models import Menu
from treemenu.config import APP_LABEL
from treemenuproj.settings import BASE_DIR

register = template.Library()


def draw_menu(context: RequestContext, menu_name: str) -> RequestContext:
    if context.request.method == 'GET' and 'active-menu' in context.request.GET:
        active_level = int(context.request.GET["level"])
        active_rank = int(context.request.GET["rank"])
    else:
        active_level, active_rank = None, None

    menu_items_fl = Menu.objects.get(name=menu_name).root_item.get_flattened()

    context['menu_name'] = menu_name

    menu_items = []

    for item in menu_items_fl:
        if active_level == None and active_rank == None:
            if item.caption == 'root_' + menu_name:
                item.caption = menu_name
                item.named_url = 'index'
                menu_items.append(item)
                break
        menu_items.append(item)

    context['menu_items'] = menu_items
    return context
register.inclusion_tag(Path(BASE_DIR, APP_LABEL, 'templates', 'menu.html'), takes_context=True)(draw_menu)
