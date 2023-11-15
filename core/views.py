from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ProcessedImage
from .utils import process_image
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ImagePath
from .serializers import ImagePathSerializer
from rest_framework import generics 


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            processed_image_path = process_image(request.FILES['original_image'])
            ProcessedImage.objects.create(original_image=request.FILES['original_image'],
                                          processed_image=processed_image_path)
            return redirect('download_image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def download_image(request):
    processed_images = ProcessedImage.objects.all()
    return render(request, 'download_image.html', {'processed_images': processed_images})


 
class ImagePathAPIView(generics.ListCreateAPIView): 
    queryset = ImagePath.objects.all() 
    serializer_class = ImagePathSerializer 