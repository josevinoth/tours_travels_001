from django.db import models
# from ..models import Product_info,Department_info,MyUser,Location_info,Vendor_info,Insurance_Info,UnitInfo

class students_info(models.Model):
    stu_name = models.CharField(max_length=50,blank=True)
    english = models.IntegerField()
    language = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.stu_name