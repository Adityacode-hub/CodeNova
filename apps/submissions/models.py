from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User=get_user_model()
# Create your models here.
class Submission(models.Model):
    type_status=[("Accepted", "Accepted"),
        ("Wrong Answer", "Wrong Answer"),
        ("TLE", "TLE"),
        ("Runtime Error", "Runtime Error"),
        ("Compilation Error", "Compilation Error"),]
    language_choices=[
        ('python','Python'),
        ('c','C'),
        ('cpp','C++'),
        ('javascipt','Javascript'),
        ('java','Java'),
        ('go','Go'),('ruby','Ruby'),
        ('rust','Rust'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    problem=models.ForeignKey('problems.Problem',on_delete=models.CASCADE)#problem app ke andr problem class
    code=models.TextField()
    language=models.CharField(max_length=50,choices=language_choices,default='python')
    runtime=models.FloatField(null=True,blank=True)
    memory=models.IntegerField(null=True,blank=True)
    submitted_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=type_status)


class SubmissionResult(models.Model):
    submission=models.OneToOneField('Submission',on_delete=models.CASCADE)
    output=models.TextField()
    test_case_passed=models.IntegerField()
    total_test_cases=models.IntegerField()
    total_cases_failed=models.IntegerField()
    error=models.TextField(blank=True,null=True)
