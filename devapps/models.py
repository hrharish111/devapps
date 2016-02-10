from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Created_form(models.Model):
        user_key =models.ForeignKey(User)
        project_Name = models.CharField(max_length=100,unique = True)
        specification = models.CharField(max_length=100)
        storage = models.CharField(max_length=100)
        customer = models.CharField(max_length=100)
        summary = models.CharField(max_length=100)
        instance_type = models.CharField(max_length=100)
        s3backet = models.CharField(max_length=100)
        db_access = models.CharField(max_length=100)
        stack = models.CharField(max_length=100)
        server_access = models.CharField(max_length=100)

        def __str__(self):
            return self.project_Name
        
class Project_data(models.Model):
    instance_name = models.CharField(max_length =100,unique = True)
    region = models.CharField(max_length=100)
    instance_id = models.CharField(max_length =100)
    instance_state = models.CharField(max_length = 100)
    instance_ip = models.CharField(max_length = 100)
    instance_type = models.CharField(max_length=100)
  
    def __str__(self):
        return self.instance_name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
