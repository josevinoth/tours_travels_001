from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    # path('asset_insert', views.assetinfo_add,name='asset_insert'),#Add Asset
    # path('asset_update/<int:asset_id>/', views.assetinfo_add,name='asset_update'),#Update asset
    # path('asset_delete/<int:asset_id>/',views.asset_delete,name='asset_delete'), #Delete asset
    # path('asset_list/',views.asset_list,name='asset_list'), #List Asset
]