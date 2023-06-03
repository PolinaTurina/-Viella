from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
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
def price_view(request, page_number = 1):
    massage = Massage.objects.all()

    paginator = Paginator(massage, 4)

    try: 
        page_obj = paginator.page(page_number)
    except EmptyPage:
        if  page_number < 1:
            page_obj = paginator.page(1)
        else:
            page_obj = paginator.page(paginator.num_pages) 

    context = {"massage_list": page_obj} 
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

