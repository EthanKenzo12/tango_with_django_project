from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from rango.models import ImageUpload, Category, Page
from rango.forms import CategoryForm, UserForm, UserProfileForm
from django.urls import reverse
from rango.forms import PageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    visits = request.session.get('visits', 0)
    last_visit = request.session.get('last_visit')

    if last_visit:
        last_visit_time = datetime.strptime(last_visit, '%Y-%m-%d %H:%M:%S.%f')
    else:
        last_visit_time = None
    if not last_visit_time or (datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['visits'] = visits
        request.session['last_visit'] = str(datetime.now())
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    'categories': category_list,
                    'pages': page_list,
                    'visits': visits}
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


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirects user to gallery after upload
    else:
        form = ImageUploadForm()

    return render(request, 'rango/upload.html', {'form': form})


@login_required
def gallery(request):
    images = ImageUpload.objects.all()
    return render(request, 'rango/gallery.html', {'images': images})


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('rango:index')
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    return render(request, 'rango/add_page.html', {'form': form, 'category': category})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('rango:index')
            else:
                return render(request, 'rango/login.html', {'error_message': 'Your account is disabled.'})
        else:
            return render(request, 'rango/login.html', {'error_message': 'Invalid login details.'})

    return render(request, 'rango/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('rango:index')


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')
