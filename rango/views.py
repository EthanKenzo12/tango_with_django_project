from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageUpload

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('gallery')  # Redirects user to gallery after upload
#     else:
#         form = ImageUploadForm()
#
#     return render(request, 'rango/upload.html', {'form': form})
#
#
# def gallery(request):
#     images = ImageUpload.objects.all()
#     return render(request, 'rango/gallery.html', {'images': images})
#
