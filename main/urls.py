from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('prayer/',prayer,name='about'),
    path('save_prayer/',save_prayer,name='save_prayer'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)