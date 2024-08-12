from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('home', views.home,name='home'),
    path('registration_add', views.registrion_add,name='registration_add'),#Add registration
    path('gender_add', views.gender_add, name='gender_add'),
    path('marks_update/<int:registration_id>/', views.marks_add,name='marks_update'),#Update registration
    path('marks_delete/<int:registration_id>/',views.marks_delete,name='marks_delete'), #Delete asset
    path('marks_list',views.marks_list,name='marks_list'), #List registration
    path('marks_add', views.marks_add, name='marks_add'),  # Add students

]