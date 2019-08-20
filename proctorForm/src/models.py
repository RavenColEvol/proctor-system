from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
	is_teacher = models.BooleanField(default = False)
	is_student = models.BooleanField(default = False)
	is_hod = models.BooleanField(default = False)
	profile_pic = models.ImageField(upload_to = 'profile_pics/',blank = True)

class Department(models.Model):
	department_choices = (
		('COMPS','Computer Science'),
		('INFT','Information Technology'),
		('MECH','Mechanical Engineering'),
		('EXTC','Electronics And Telecommunications Enginnering'),
		('INST','Instrumentation Enginnering'),
		('Civil','Civil Engineering'),
		('ASH','Applied Science And Humanities'),
	)
	department_name = models.CharField(max_length = 50 , choices = department_choices)

	def __str__(self):
   		return self.department_name

	def get_absolute_url(self):
		return reverse('proctor_view',kwargs={'id':self.id})

class Proctor(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	proc_department = models.ForeignKey(Department, on_delete = models.CASCADE)
	proctor_about = models.CharField(max_length = 300)
	proctor_contact = models.IntegerField()
	

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('proctor_view',kwargs={'id':self.id})


class Student(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	student_contact = models.IntegerField()
	student_address = models.TextField()
	student_interest = models.TextField()
	student_extracurricular = models.TextField()
	proctor_id = models.ForeignKey(Proctor, on_delete=models.CASCADE)
	student_sem1 = models.FloatField(default = 0)
	student_sem2 = models.FloatField(default = 0)
	student_sem3 = models.FloatField(default = 0)
	student_sem4 = models.FloatField(default = 0)
	student_sem5 = models.FloatField(default = 0)
	student_sem6 = models.FloatField(default = 0)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('student_details',kwargs={'id':self.id})


class Messages(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	message = models.CharField(max_length=150)
	timestamp = models.TimeField(auto_now=True)

	class Meta:
		verbose_name = 'Message'
		verbose_name_plural = 'Messages'

	def __str__(self):
		return self.user.username


