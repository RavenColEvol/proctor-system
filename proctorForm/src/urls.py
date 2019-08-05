from django.urls import path
from src import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.index,name='home'),
	path('department/',views.department_view,name='department_view'),
	path('proctor/',views.proctor_view,name='proctor_view'),
	path('student/',views.student_view,name='student_view'),
	path('proctor_form/',views.StudentForm.as_view(),name='proctor_form'),
	path('student_signup_form/',views.StudentSignUp.as_view(),name='student_signup'),

    #authentication
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',views.logout_user,name='logout')
	#path('proctor_update_form/<int:pk>',views.StudentUpdateForm.as_view(),name='proctor_update_form'),
]
