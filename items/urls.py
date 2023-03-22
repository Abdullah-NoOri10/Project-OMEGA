from django.urls import path
from . import views

urlpatterns = [
    path("", views.comps, name='home'),
    path("profile/<str:pk>", views.profile, name='profile'),
    path("form/", views.create_product, name='create-product'),
    path("sign-in/", views.login, name='login'),
    path("error/", views.error_page, name='error'),
    path("sign-out/", views.sign_out, name='sign-out'),
    path("sign-up/", views.sign_up, name='sign-up'),
    path("product/", views.product, name='product'),

]
