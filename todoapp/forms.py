from django import forms
from todoapp.models import Todos,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodoForm(forms.ModelForm):

    # options=(
    #     (True,True),
    #     (False,False)
    # )
    # status=forms.ChoiceField(choices=options)
    class Meta:
        model=Todos
        fields=["task_name",

                ]
class TodoUpdateForm(forms.ModelForm):
    options = (
        (True,True),
        (False,False)
    )
    status=forms.ChoiceField(choices=options)

    class Meta:
        model=Todos
        fields=[
            'task_name',
        ]
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=[
            'profile_pic',
            'date_of_birth',
            'phone'
        ]
        widgets={
            'date_of_birth':forms.DateInput(attrs={'class':'forms-control','type':'date'})
        }

