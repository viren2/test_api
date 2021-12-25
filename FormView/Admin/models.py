from django.db import models

# Create your models here.
class  Admin(models.Model):
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email    = models.EmailField(max_length=50)
    mobile_no = models.IntegerField()
    def __str__(self):
        return " username is "+self.username +" last name is "+self.last_name
