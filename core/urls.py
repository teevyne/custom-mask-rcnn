from django.urls import path
from .views import upload_image, download_image, ImagePathAPIView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('upload/', upload_image, name='upload_image'),
    path('download/', download_image, name='download_image'),
    path('image-download/', ImagePathAPIView.as_view())
]