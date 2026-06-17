from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Products Sub-pages
    path('products/roller-blinds/', views.roller_blinds, name='roller_blinds'),
    path('products/zebra-blinds/', views.zebra_blinds, name='zebra_blinds'),
    path('products/wooden-blinds/', views.wooden_blinds, name='wooden_blinds'),
    path('products/other-blinds/', views.other_blinds, name='other_blinds'),
    
    path('gallery/', views.gallery, name='gallery'),
    path('get-quote/', views.get_quote, name='get_quote'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    
    # Post Request Url
    path('contact-enquiry/', views.contact_enquiry, name='contact_enquiry'),
    path('home-enquiry/', views.home_enquiry, name='home_enquiry'),
    path('quote-request/', views.quote_request, name='quote_request'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)