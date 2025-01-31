from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .models import ImageUpload

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the DjangoApp homepage!")


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirects user to gallery after upload
    else:
        form = ImageUploadForm()

    return render(request, 'DjangoApp/upload.html', {'form': form})


def gallery(request):
    images = ImageUpload.objects.all()
    return render(request, 'DjangoApp/gallery.html', {'images': images})

