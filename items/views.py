from django.shortcuts import render, redirect
from .models import Product, Companie, User, Category
from .forms import CreateProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def comps(request):

    names = Companie.objects.only('name')
    catagories = Category.objects.all()[0:8]
    user = request.user
    product = Product.objects.all()[0:8]

    context = {'names': names, 'catagories': catagories,
               'user': user, 'product': product}
    return render(request, 'home.html', context)


def profile(request, pk):
    company = Companie.objects.get(id=pk)
    products = company.product_set.all()
    context = {'company': company, 'products': products}
    return render(request, 'profile.html', context)


def create_product(request):
    form = CreateProductForm

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        product = request.POST.get('product')

        product = Product.objects.create(

        )

    return render(request, 'createproduct.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            return redirect('home')
        else:
            return redirect('error')

    context = {}
    return render(request, 'login.html', context)


def error_page(request):
    context = {}
    return render(request, 'error.html', context)


def sign_out(request):
    logout(request)
    context = {}
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login_user(request, user)
        return redirect('home')

    context = {}
    return render(request, 'sign_up.html', context)


@login_required(login_url='login')
def product(request):
    # product = Product.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    product = Product.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(price__icontains=q)
    )

    catagories = Category.objects.all()[0:8]


    context = {'product': product, 'catagories': catagories}

    return render(request, 'product.html', context)
