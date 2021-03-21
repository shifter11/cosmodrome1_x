from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def filmmaking(request):
    return render(request, 'main/filmmaking.html')

def contact_us(request):
    return render(request, 'main/contact.html')