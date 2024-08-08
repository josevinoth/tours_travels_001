from django.contrib import admin
from .models import registration_info
from .models import marks_info


# Register your models here.
admin.site.register(registration_info)
admin.site.register(marks_info)
