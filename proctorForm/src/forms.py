from django import forms
from .models import Student
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.auth.forms import UserCreationForm
from .models import Student, User

class ProctorForm(forms.ModelForm):
	sem_pointers = SimpleArrayField(forms.IntegerField())
	class Meta:
		model = Student
		exclude = ['user',]

class StudentSignUpForm(UserCreationForm):	
	class Meta(UserCreationForm.Meta):
		model=User

	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.save()
		return user

class TeacherSignUpForm(UserCreationForm):	
	class Meta(UserCreationForm.Meta):
		model=User

	def save(self):
		user = super().save(commit=False)
		user.is_teacher = True
		user.save()
		return user


