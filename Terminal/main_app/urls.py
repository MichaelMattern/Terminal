# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                # Home page
    path('account/', views.account, name='account'),    # Account page
    path('company/', views.company, name='company'),    # Company page
    path('tools/', views.tools, name='tools'),          # Tools page
    path('stock-search/', views.stock_search_view, name='stock_search'),
]
