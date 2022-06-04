from django.db import models
from django.contrib.auth.models import User

class Todos(models.Model):
  task_name=models.CharField(max_length=120)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  date=models.DateField(auto_now_add=True)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.task_name

class UserProfile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
  profile_pic=models.ImageField(upload_to="images")
  date_of_birth=models.DateField(null=True)
  phone=models.CharField(max_length=12)



#ORM querries
#object relational mappers
#ORM querry for creating a resource
#ref_name=Model_name(field1=value,field2=value,field3=value)
#ref_name=save()

#ORM query for fetching all records
#reference name=model name.objects.all()
#qs=Todos.objects.all()

#filtering ORM querries
#qs=Todos.objects.filter(status=True)