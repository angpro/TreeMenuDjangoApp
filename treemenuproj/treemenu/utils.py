from django.utils.safestring import mark_safe
from django.forms import ChoiceField

from treemenu.models import MenuItem


def clean_ranks(menu_items):
    """
    Resets ranks from 0 to n, n being the number of items.
    """
    rank = 0
    for menu_item in menu_items:
        menu_item.rank = rank
        menu_item.save()
        rank += 1