from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def myaccount(request):
    return render(request, 'my-account.html')

def orderstatus(request):
    return render(request, 'orderstatus.html')

def newproduct(request):
    return render(request, 'newproduct.html')

def allproducts(request):
    return render(request, 'allproducts.html')

def favourite(request):
    return render(request, 'favourite.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def checkout(request):
    return render(request, 'checkout.html')