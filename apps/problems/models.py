from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.text import slugify
User=get_user_model()
# Create your models here.

class Tags(models.Model):
    name=models.CharField(max_length=60,unique=True)
    slug=models.SlugField(unique=True)

class Problem(models.Model):
    difficulty_level=[('Easy','Easy'),
                      ('Medium','Medium'),
                      ('Hard','Hard'),
                      
                      
                      
                      ]
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)#slug is used like two-sum-problem etc
    difficulty=models.CharField(max_length=10,choices=difficulty_level,default='Easy')
    tags=models.ManyToManyField('Tags',related_name='problem')
    description=models.TextField()
    input_format=models.TextField()
    output_format=models.TextField()
    sample_input=models.TextField()
    sample_output=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)# if the user gets deleted the preoblem remains in the system
    created_on=models.TimeField(auto_created=timezone.now)
    def __str__(self):
        return self.title
    


#difference between set null and cascasde is  ownership lost then in cascade delete forever

#not recommendable for the big scale project
