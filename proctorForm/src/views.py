from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .forms import ProctorForm
from .models import Student
# Create your views here.
def index(request):
	return render(request,'src/index.html',{})

def student_view(request):
	return render(request,'src/student.html',{})

def proctor_view(request):
	return render(request,'src/proctor.html',{})

def department_view(request):
	return render(request,'src/department.html',{})

def student_form(request):
	form = ProctorForm()
	return render(request,'src/forms/student_form.html',{'form':form})

class StudentForm(CreateView):
	model = Student
	fields = '__all__'

class StudentUpdateForm(UpdateView):
	model = Student
	fields = '__all__'
	template_name_suffix = '_update_form'
