from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('price/<int:page_number>/', price_view, name='prices'),
    # path('', main_view, name='main'),
    path('', modal_view, name='main')
]
