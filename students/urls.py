from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.main,name='main'),
    path('students/',views.student,name='students'),
    path('students/details/<int:id>', views.details, name='details'),
    path('upload/',views.upload),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    
    
