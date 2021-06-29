from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
