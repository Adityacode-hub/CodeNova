from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
class CustomUserManger(BaseUserManager):
  def create_user(self,email,phone,date_of_birth,password=None):
   
    if not email:
       raise ValueError("User must have an email address")
    user=self.model(email=self.normalize_email(email),date_of_birth=date_of_birth,phone=phone,)
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self,email,phone,date_of_birth,password=None):
     user=self.create_user(email=email,phone=phone,password=password,date_of_birth=date_of_birth)
     user.is_admin=True
     user.is_superuser=True
     user.is_staff=True
     user.save(using=self._db)
     return user
  
class CustomUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email address",max_length=255,unique=True)
    phone=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg', null=True, blank=True)
      
    is_active = models.BooleanField(default=True)#user should be active during creation
    is_admin = models.BooleanField(default=False)#Only used if you added custom admin logic (not needed usually)
    is_superuser = models.BooleanField(default=False)#	Only a few trusted users should be superusers
    is_staff = models.BooleanField(default=False)#normal user cannot get admin access


    objects=CustomUserManger()

    
    USERNAME_FIELD="email"#authenticate will work on this field only
    REQUIRED_FIELDS=["phone","date_of_birth"]
    def __str__(self):
       return self.email
    def has_perm(self,perm,obj=None):
       return self.is_superuser
    def has_module_perms(self,app_label):
       return self.is_superuser
   
    def is_staff(self):

       return self.is_admin
    
   
