from django.db import models

class ContactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class HomeEnquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    subject = models.CharField(max_length=200)
    control_type = models.CharField(max_length=200, blank=True)

    window_width = models.CharField(max_length=50, blank=True)
    window_height = models.CharField(max_length=50, blank=True)
    dimension_unit = models.CharField(max_length=20, blank=True)

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name