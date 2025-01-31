from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/') # To store images in the folder /media/uploads
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title