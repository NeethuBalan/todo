from django.db import models

# create your models here.
class Todos(models.Model):
  task_name=models.CharField(max_length=120)
  user=models.CharField(max_length=80)
  date=models.DateField(auto_now_add=True)
  status=models.BooleanField(default=False)

