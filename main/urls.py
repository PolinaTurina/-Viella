from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('price/<int:page_number>/', price_view, name='prices'),
    path('comment/<int:page_number>/', comment_view, name='comments'),
    # path('', main_view, name='main'),
    path('', modal_view, name='main'),

]
