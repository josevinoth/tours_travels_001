from django.db import models
from ..models import registration_info

class students_info(models.Model):
    stu_name = models.ForeignKey(registration_info, on_delete=models.CASCADE, default='')
    english = models.IntegerField()
    language = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.stu_name