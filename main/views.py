from django.shortcuts import render


def main_view(request):
    return render(request, 'main/main.html')

def talons_sertificats_view(request):
    return render(request, 'main/talons_sertificats.html')

def stop_view(request):
    return render(request, 'main/stop.html')

def price_view(request):
    return render(request, 'main/price.html')

def about_view(request):
    return render(request, 'main/about.html')

def comment_view(request):
    return render(request, 'main/comment.html')

def contact_view(request):
    return render(request, 'main/contact.html')