from django.contrib import admin
from .models import HomeEnquiry, ContactEnquiry,QuoteRequest

admin.site.register(HomeEnquiry)
admin.site.register(ContactEnquiry)
admin.site.register(QuoteRequest)