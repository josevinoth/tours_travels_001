from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('registration_add', views.registrion_add,name='registration_add'),#Add Asset
    path('students_add', views.students_add, name='students_add'),  # Add Asset
    # path('asset_update/<int:asset_id>/', views.assetinfo_add,name='asset_update'),#Update asset
    # path('asset_delete/<int:asset_id>/',views.asset_delete,name='asset_delete'), #Delete asset
    # path('asset_list/',views.asset_list,name='asset_list'), #List Asset
]