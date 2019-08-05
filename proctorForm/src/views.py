from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from src.forms import ProctorForm,StudentSignUpForm,TeacherSignUpForm
from src.models import Student,User
from django.contrib.auth import login,logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
	return render(request,'src/index.html',{})

def student_view(request):
	return render(request,'src/student.html',{})

def proctor_view(request):
	return render(request,'src/proctor.html',{})

def department_view(request):
	return render(request,'src/department.html',{})


class StudentForm(CreateView):
    model=Student
    form_class = ProctorForm
    
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('home')

class StudentUpdateForm(UpdateView):
	model = Student
	fields = '__all__'
	template_name_suffix = '_update_form'

class StudentSignUp(CreateView):
	model=User
	form_class = StudentSignUpForm
	template_name = 'src/forms/student_form.html'

	def form_valid(self,form):
		user = form.save()
		login(self.request,user)
		return redirect('home')

class TeacherSignUp(CreateView):
	model=User
	form_class = TeacherSignUpForm
	template_name = 'src/forms/teacher_form.html'

	def form_valid(self,form):
		user = form.save()
		login(self.request,user)
		return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')
