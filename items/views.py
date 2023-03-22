from django.shortcuts import render, redirect
from .models import Product, Companie, User,Category
from .forms import CreateProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def comps(request):
    user = request.user
    names = Companie.objects.only('name')
    catagories = Category.objects.all()[0:8]
    list_catagories = Category.objects.all()
    product = Product.objects.all()[0:8]
    context = {'names': names,'catagories':catagories,'product':product,'user':user,'list_catagories':list_catagories}
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
            return redirect('companies')
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
    return redirect('companies')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        login_user(request,user)
        return redirect('companies')

    context = {}
    return render(request,'sign_up.html',context)


def product(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    product = Product.objects.filter(Q(name__icontains=q)|
                                    Q(category__name__icontains=q))
    context = {'product':product}
    return render(request,'product.html',context)