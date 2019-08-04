from django.urls import path
from src import views


urlpatterns = [
	path('',views.index,name='home'),
	path('department/',views.department_view,name='department_view'),
	path('proctor/',views.proctor_view,name='proctor_view'),
	path('student/',views.student_view,name='student_view'),
	path('proctor_form/',views.StudentForm.as_view(),name='proctor_form'),
	#path('proctor_update_form/<int:pk>',views.StudentUpdateForm.as_view(),name='proctor_update_form'),
]