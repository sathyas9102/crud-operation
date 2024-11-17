from django.db import models

# Create your models here.

class Login(models.Model):
    Username=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    PhoneNo=models.CharField(max_length=15)
    
    def __str__(self):
        return "%S" %(self.Username)
    
    class Meta:
        db_table="task1"