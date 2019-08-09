from django.urls import path
from . import views

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.index,name='home'),
	path('department/',views.department_view.as_view(),name='department_view'),
	path('proctor/<int:id>',views.proctor_view.as_view(),name='proctor_view'),
	path('proctor_details/<int:id>',views.proctor_details.as_view(),name='proctor_details'),
	path('student/',views.student_view,name='student_view'),
	path('proctor_form/',views.StudentForm.as_view(),name='proctor_form'),
	path('student_signup_form/',views.StudentSignUp.as_view(),name='student_signup'),
	path('teacher_signup_form/',views.TeacherSignUp.as_view(),name='teacher_signup'),

    #authentication
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',views.logout_user,name='logout')
	#path('proctor_update_form/<int:pk>',views.StudentUpdateForm.as_view(),name='proctor_update_form'),
]
