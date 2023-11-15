# image_processing_app/models.py
from django.db import models

class ProcessedImage(models.Model):
    original_image = models.ImageField(upload_to='uploads/')
    processed_image = models.ImageField(upload_to='processed/')


class ImagePath(models.Model):
    image_path = models.CharField(max_length=255)
