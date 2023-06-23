from typing import Any
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from .models import *
from .forms import *


from django.contrib import messages
from django.contrib.auth import login, logout


"""главная страница"""
def main_view(request):
    massage = Massage.objects.all() 
    context = {'massage_list': massage}
    return render(request, 'main/main.html', context)


"""обработчик формы в модальном окне"""
def modal_view(request):
    
    context = {}
    if request.method == 'POST':
        form = TalonForm(request.POST)
        if form.is_valid():
            context = {'success': 1}
            form = TalonForm
    else:
        form = TalonForm()
    context['form2'] = form
    return render(request,'main/main.html', context=context)
    


""" страница талоны и сертификаты"""
def talons_sertificats_view(request):
    sertificats = Sertificats.objects.all()
    context = {"sert": sertificats}

    if request.method == 'POST':
        form = SertForm(request.POST)
        if form.is_valid():
            send_sert(form.cleaned_data['name'], form.cleaned_data['phone'], form.cleaned_data['email'], )
            context = {'success': 1}
            form = SertForm
    else:
        form = SertForm()
    context ['form'] = form
    return render(request, 'main/talons_sertificats.html', context,)

def send_sert(phone, email, name):
    pass


"""страница противопоказания"""
def stop_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        stop = Stop.objects.filter(text__icontains=q)
    else:
        stop = Stop.objects.all()
    context = {"stop_list": stop}
    
    
    return render(request, 'main/stop.html', context)


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



"""обработка картинок на странице прайс"""
def img_view(request):
    context = {'image': Img.all()}
    return render (request, 'price.html', context)


"""обработка аватарок на странице с отзывами"""
def user_view(request):
    context = {'image': Img.all()}
    return render (request, 'comment.html', context)



"""страница о нас"""
def about_view(request):
    return render(request, 'main/about.html')


"""страница отзывы"""
def comment_view(request, page_number = 1):
    context = {}
    comments = Comments.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm()
    else:
        form = CommentForm()
        context ['comment_form'] = form


        
    paginator = Paginator(comments, 3)
    try:
            page_obj = paginator.page(page_number)
    except Exception:
            if page_number < 1:
                page_obj = paginator.page(1)
            else:
                page_obj = paginator.page(paginator.num_pages) 
    return render(request, 'main/comment.html', {'comments':comments, 'comment_form':form, 'page_comments':page_obj},)



"""страница контакты"""
def contact_view(request):
    return render(request, 'main/contact.html')



"""страница авторизация"""
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('main:main')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'login_form':form})


def user_logout(request):
    logout(request)
    return redirect ('login')



"""страница регистрация"""
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистраиця прошла успешно!')
            return redirect ('main:main')
        else: 
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'reg_form':form})

