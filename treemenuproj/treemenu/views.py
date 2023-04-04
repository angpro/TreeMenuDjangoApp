from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    context = {
    }
    template = 'index.html'
    return render(request, template, context)


def menu_content(request: HttpRequest) -> HttpResponse:
    context = {
        'active_menu': request.GET["active-menu"],
        'active_level': int(request.GET["level"]), 
        'active_rank': int(request.GET["rank"]),
        'active_parent': request.GET["parent"],
        #'do_draw': True,
    }
    template = 'index.html'
    return render(request, template, context)

