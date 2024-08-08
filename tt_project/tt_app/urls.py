from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('registration_add', views.registrion_add,name='registration_add'),#Add registration
    path('marks_add', views.marks_add, name='marks_add'),  # Add students
    # path('asset_update/<int:asset_id>/', views.assetinfo_add,name='asset_update'),#Update asset
    # path('asset_delete/<int:asset_id>/',views.asset_delete,name='asset_delete'), #Delete asset
    path('registration_list', views.registration_list, name='registration_list'), #List registration
]