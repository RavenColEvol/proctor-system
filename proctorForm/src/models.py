from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(AbstractUser):
	is_teacher = models.BooleanField(default = False)
	is_student = models.BooleanField(default = False)
	is_hod = models.BooleanField(default = False)
	#profile_pic = models.ImageField(upload_to = 'profile_pics/',blank = True)

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


class Proctor(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	# proctor_name = models.CharField(max_length = 150) we can use first_name , last_name from user class
	proctor_about = models.CharField(max_length = 300)
	proctor_contact = models.IntegerField()
	# proctor_image = models.ImageField() we can user profile_pic from user

	def __str__(self):
		return self.user


class Student(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	student_id = models.IntegerField() # i think we can use username from class'user' intead of creating new attribute
	# student_name = models.CharField(max_length = 150)
	student_contact = models.IntegerField()
	student_address = models.TextField()
	student_interest = models.TextField()
	student_extracurricular = models.TextField()
	# student_image = models.ImageField()
	proctor_id = models.ForeignKey(Proctor, on_delete=models.CASCADE)
	sem_pointer =  ArrayField(models.IntegerField(default = 0),null = True, size = 8)
	#student_sem1 = models.IntegerField()
	#student_sem2 = models.IntegerField()
	#student_sem3 = models.IntegerField()
	#student_sem4 = models.IntegerField()
	#student_sem5 = models.IntegerField()
	#student_sem6 = models.IntegerField()

	def __str__(self):
		return self.user
