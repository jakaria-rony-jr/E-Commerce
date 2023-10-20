from django.shortcuts import render
from .models import *

def index(request):
    product = Products.objects.all()
    F_product = FeaturedProducts.objects.all()
    B_banner = Banner.objects.all()
    S_banner = SectionBanner.objects.all()
    B_seller = BestSeller.objects.all()
    featured = Featured.objects.all()
    offer = SpecialOffer.objects.all()
    L_banner = LastBanner.objects.all()
    client = OurClient.objects.all()
    services = Services.objects.all()

    context = {
        'product':product,
        'F_product':F_product,
        'B_banner':B_banner,
        'S_banner':S_banner,
        'B_seller':B_seller,
        'featured':featured,
        'offer':offer,
        'L_banner':L_banner,
        'client':client,
        'services':services

    }

    return render(request, 'user_app/index.html', context)

def compare(request):
    return render(request, 'user_app/compare.html')

def login(request):
    return render(request, 'user_app/login.html')

def signup(request):
    return render(request, 'user_app/signup.html')

def wishlist(request):
    return render(request, 'user_app/wishlist.html')