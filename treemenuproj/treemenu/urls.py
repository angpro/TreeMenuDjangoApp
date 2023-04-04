from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('page-a-1', views.menu_content, name='page_a_1'),
    path('page-a-1-1', views.menu_content, name='page_a_1_1'),
    path('page-a-1-1-1', views.menu_content, name='page_a_1_1_1'),
    path('page-a-1-1-2', views.menu_content, name='page_a_1_1_2'),

    path('page-a-2', views.menu_content, name='page_a_2'),
    path('page-a-2-1', views.menu_content, name='page_a_2_1'),

    path('page-a-3', views.menu_content, name='page_a_3'),
    path('page-a-3-1', views.menu_content, name='page_a_3_1'),
    path('page-a-3-1-1', views.menu_content, name='page_a_3_1_1'),
]