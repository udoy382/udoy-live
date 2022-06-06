from django.db import models

# Create your models here.

# Username = udoysecurity
# password = udoysecurity436.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'