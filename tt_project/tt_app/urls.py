from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('registration_add', views.registrion_add,name='registration_add'),#Add registration
    path('resgistration_update/<int:registration_id>/', views.registrion_add,name='resgistration_update'),#Update registration
    path('resgistration_delete/<int:registration_id>/',views.registration_delete,name='resgistration_delete'), #Delete asset
    path('registration_list',views.registration_list,name='registration_list'), #List registration
    path('students_add', views.students_add, name='students_add'),  # Add students
]