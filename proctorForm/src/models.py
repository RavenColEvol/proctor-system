from django.db import models

# Create your models here.
class Department(models.Model):
	department_name = models.CharField(max_length = 50)


class Proctor(models.Model):
	proctor_name = models.CharField(max_length = 150)
	proctor_about = models.CharField(max_length = 300)
	proctor_contact = models.IntegerField()
	proctor_image = models.ImageField()


class Student(models.Model):
	student_id = models.IntegerField()
	student_name = models.CharField(max_length = 150)
	student_contact = models.IntegerField()
	student_address = models.TextField()
	student_interest = models.TextField()
	student_extracurricular = models.TextField()
	student_image = models.ImageField()
	proctor_name = models.ForeignKey(Proctor,on_delete=models.CASCADE,blank=True) 
	student_sem1 = models.IntegerField()
	student_sem2 = models.IntegerField()
	student_sem3 = models.IntegerField()
	student_sem4 = models.IntegerField()
	student_sem5 = models.IntegerField()
	student_sem6 = models.IntegerField()