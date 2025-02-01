from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageUpload


# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirects user to gallery after upload
    else:
        form = ImageUploadForm()

    return render(request, 'rango/upload.html', {'form': form})


def gallery(request):
    images = ImageUpload.objects.all()
    return render(request, 'rango/gallery.html', {'images': images})
