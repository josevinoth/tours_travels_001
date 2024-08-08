from django.contrib import admin
from .models import registration_info
from .models import students_info


# Register your models here.
admin.site.register(registration_info)
admin.site.register(students_info)
