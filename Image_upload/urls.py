from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:pk>', views.image_page, name='image_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)