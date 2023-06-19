from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from main.views import main_view, talons_sertificats_view, stop_view, price_view, about_view, comment_view, contact_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='prices'), name='main'), #
    path('main/', include('main.urls', namespace='comments'), name='comment'), #
    path('talons_sertificats/', talons_sertificats_view, name='talons_sertificats'),
    path('stop/', stop_view, name='stop'),
    path('about/', about_view, name='about'),
    # path('comment/', comment_view, name='comment'),
    path('contact/', contact_view, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

