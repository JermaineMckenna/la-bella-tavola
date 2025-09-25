from django.shortcuts import render

def home_view(request):
    return render(request, 'menu/home.html')

def menu_view(request):
    return render(request, 'menu/menu.html')

def booking_view(request):
    return render(request, 'menu/booking.html')
