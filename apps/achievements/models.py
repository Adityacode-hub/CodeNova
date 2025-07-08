from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Acheivement(models.Model):
    level_type=[

        ('noob','Noob'),
        ('ninja','Ninja'),
        ('pro','Pro'),
        ('master','Master'),
        ('grandmaster','Grandmaster')
    ]
    type_medal=[

        ('bronze','Bronze'),
        ('silver','Silver'),
        ('gold','Gold'),
        ('platinum','Platinum'),
    ]
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    rank=models.CharField(max_length=15,choices=level_type,default='noob')
    medal_type=models.CharField(max_length=10,choices=type_medal,null=True,blank=True)
    description=models.TextField()
    Badge=models.CharField(max_length=10,choices=type_medal,null=True,blank=True)