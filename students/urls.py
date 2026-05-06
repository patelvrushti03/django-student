from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.main,name='main'),
    path('students/',views.student,name='students'),
    path('', views.home, name='home'),
    path('students/details/<int:id>', views.details, name='details'),
    path('upload/',views.upload),
    path('dashboard/',views.dashboard,name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    