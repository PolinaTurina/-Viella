from django.urls import path
from main.views import price_view, main_view

app_name = 'main'

urlpatterns = [
    path('price/<int:page_number>/', price_view, name='prices'),
    path('', main_view, name='main'),
]