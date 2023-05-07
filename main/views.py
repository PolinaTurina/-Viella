from django.shortcuts import render
from .models import Massage


"""главная страница"""
def main_view(request):
    return render(request, 'main/main.html')


""" страница талоны и сертификаты"""
def talons_sertificats_view(request):
    return render(request, 'main/talons_sertificats.html')


"""страница противопоказания"""
def stop_view(request):
    return render(request, 'main/stop.html')


"""страница прайс"""
def price_view(request):
    massage = Massage.objects.all()
    context = {"massage_list": massage}
    return render(request, 'main/price.html', context)

def img_view(request):
    context = {'image': Img.all()}
    return render (request, 'price.html', context)


"""страница о нас"""
def about_view(request):
    return render(request, 'main/about.html')


"""страница отзывы"""
def comment_view(request):
    return render(request, 'main/comment.html')


"""страница контакты"""
def contact_view(request):
    return render(request, 'main/contact.html')