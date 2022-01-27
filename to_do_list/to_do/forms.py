from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class TaskForm(forms.ModelForm):
    due_date=forms.SplitDateTimeField()
    class Meta:
        model=models.Task
        exclude=['owner']
        #widgets={"due_date":forms.SplitDateTimeWidget}




class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = '__all__'#['username', 'email', 'first_name', "password_1","password_2"]
