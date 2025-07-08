from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model();
class Streaks(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    Current_streak_Count=models.IntegerField(default=0)
    max_streak=models.IntegerField(default=0)
    last_submission=models.DateTimeField(null=True)
    def __str__(self):
        return f"{self.User.username}-current:{self.Current_streak_Count},Max:{self.max_streak}"
    