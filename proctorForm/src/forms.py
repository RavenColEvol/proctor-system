from django import forms
from django.contrib.auth.forms import UserCreationForm
from src.models import Student, User
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

class TeacherSignUpForm(UserCreationForm):	
	class Meta(UserCreationForm.Meta):
		model=User

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_teacher = True
		user.save()
		return user


