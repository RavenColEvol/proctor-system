from django import forms
from .models import Student

from django.contrib.auth.forms import UserCreationForm
from .models import Student, User
from django.db import transaction

class ProctorForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['user',]

class StudentSignUpForm(UserCreationForm):	
	class Meta(UserCreationForm.Meta):
		model=User

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.save()
		return user


