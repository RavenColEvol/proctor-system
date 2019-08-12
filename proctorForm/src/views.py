from django.shortcuts import render ,get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .decorators  import teacher_required,hod_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ProctorForm,StudentSignUpForm,TeacherSignUpForm
from .models import Student, User, Department, Proctor

from django.contrib.auth import login,logout

# Create your views here.
def index(request):
	return render(request,'src/index.html',{})

def student_view(request):
	return render(request,'src/student.html',{})


def dashboard(request):
	students_under_teacher = Student.objects.filter(proctor_id__user = request.user)
	return render(request,'src/dashboard.html',{'students':students_under_teacher})

class proctor_view(ListView):
	template_name = 'src/proctor.html'
	def get_queryset(self):
		id_ = self.kwargs.get("id")
		return get_list_or_404(Proctor,proc_department = id_)

class department_view(ListView):
	template_name = 'src/department.html'
	def get_queryset(self):
	 return Department.objects.order_by('department_name')

class proctor_details(DetailView):
	template_name = 'src/proctor_details.html'
	def get_object(self, queryset=None):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Proctor,id = id_)

@method_decorator(teacher_required, name='dispatch')
class student_details(LoginRequiredMixin,DetailView):
	login_url = '/login/'
	template_name = 'src/student_details.html'
	def get_object(self, queryset=None):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Student,id = id_)

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


@method_decorator(hod_required, name='dispatch')
class TeacherSignUp(LoginRequiredMixin,CreateView):
	login_url = '/login/'
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
