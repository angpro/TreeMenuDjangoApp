from pathlib import Path
from typing import Optional

from django import template
from django.template import RequestContext

from treemenu.models import Menu, MenuItem
from treemenu.config import APP_LABEL
from treemenuproj.settings import BASE_DIR

register = template.Library()


# @register.simple_tag()
# def update_variable(value):
#     return value


def draw_menu(context: RequestContext, menu_name: str) -> RequestContext:
    if context.request.method == 'GET' and 'active-menu' in context.request.GET:
        active_menu = context.request.GET["active-menu"]
        active_level = int(context.request.GET["level"])
        active_rank = int(context.request.GET["rank"])
        active_parent = context.request.GET["parent"]
    else:
        active_menu, active_level, active_rank, active_parent = None, None, None, None

    menu_items_fl = Menu.objects.get(name=menu_name).root_item.get_flattened()

    context['menu_name'] = menu_name
    context['menu_items_fl'] = menu_items_fl

    menu_items_fl_to_draw = []
    # context[menu_name][node_caption] = []

    for item in menu_items_fl:
        if active_level == None and active_rank == None:
            if item.caption == 'root_' + menu_name:
                item.caption = menu_name
                item.named_url = 'index'
                menu_items_fl_to_draw.append(item)
                break
        
        if active_level == 0 and active_rank == 0:
            if item.level == 0:
                continue
            menu_items_fl_to_draw.append(item)
            continue

        if item.level == 1:
            menu_items_fl_to_draw.append(item)
            node_caption = item.caption
            continue
        
        # if node_caption:
        #     get_node_children(context, node_caption, menu_items_fl)
        #     print(context[node_caption])

    context['menu_items_fl_to_draw'] = menu_items_fl_to_draw
    return context
register.inclusion_tag(Path(BASE_DIR, APP_LABEL, 'templates', 'menu.html'), takes_context=True)(draw_menu)


def draw_menu_item(context: RequestContext, menu_item: MenuItem, do_draw: Optional[bool]=None) -> RequestContext:
#     print('Call draw menu item')

#     if not isinstance(menu_item, MenuItem):
#         error_message = 'Given argument must be a MenuItem object.'
#         raise template.TemplateSyntaxError(error_message)

#     context['menu_item'] = menu_item

#     if (do_draw == None):
#         context['do_draw'] = True    
#     else:
#         context['do_draw'] = do_draw
#     print(context['do_draw'])
    return context
register.inclusion_tag(Path(BASE_DIR, APP_LABEL, 'templates', 'menu_item.html'), takes_context=True)(draw_menu_item)
