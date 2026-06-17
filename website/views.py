from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ContactEnquiry, HomeEnquiry,QuoteRequest

# 1. Home
def home(request):
    return render(request, 'home.html')

# 2. About
def about(request):
    return render(request, 'about.html')

# 3. Product Pages
def roller_blinds(request):
    return render(request, 'products/roller_blinds.html')

def zebra_blinds(request):
    return render(request, 'products/zebra_blinds.html')

def wooden_blinds(request):
    return render(request, 'products/wooden_blinds.html')

def other_blinds(request):
    return render(request, 'products/other_blinds.html')

# 7. Gallery
def gallery(request):
    return render(request, 'gallery.html')

# 8. Get Quote
def get_quote(request):
    return render(request, 'get_quote.html')

# 9. FAQs
def faqs(request):
    return render(request, 'faqs.html')

# 10. Contact
def contact(request):
    return render(request, 'contact.html')







def contact_enquiry(request):
    if request.method == "POST":
        ContactEnquiry.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )

        messages.success(
            request,
            "Thank you! Your enquiry has been submitted successfully."
        )

    return redirect('home')

def home_enquiry(request):
    if request.method == "POST":
        HomeEnquiry.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message")
        )

        messages.success(
            request,
            "Thank you! Your enquiry has been submitted successfully."
        )

    return redirect('home')

def quote_request(request):
    if request.method == "POST":
        QuoteRequest.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            control_type=request.POST.get("control_type"),
            window_width=request.POST.get("window_width"),
            window_height=request.POST.get("window_height"),
            dimension_unit=request.POST.get("dimension_unit"),
            message=request.POST.get("message"),
        )

        messages.success(
            request,
            "Your quote request has been submitted successfully."
        )

    return redirect('get_quote')