from django.db import models
class Admission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    course = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    state = models.CharField(max_length=100, default='Maharashtra')
    district = models.CharField(max_length=100, default='Kolhapur')
    subdistrict = models.CharField(max_length=100, default='Hatkanangale')
    city = models.CharField(max_length=100, default='Kolhapur')
    pincode = models.CharField(max_length=6, default='416003')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
