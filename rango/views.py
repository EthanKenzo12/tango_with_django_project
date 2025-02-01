from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageUpload, Category, Page


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    'categories': category_list,
                    'pages': page_list, }
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        category = None
        pages = None

    context_dict = {
        'category': category,
        'pages': pages,
    }

    return render(request, 'rango/category.html', context_dict)


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
