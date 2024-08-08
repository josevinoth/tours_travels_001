from django.db import models
# from ..models import Product_info,Department_info,MyUser,Location_info,Vendor_info,Insurance_Info,UnitInfo

class marks_info(models.Model):
    reg_name = models.CharField(max_length=50,blank=True)
    reg_English = models.IntegerField()
    reg_Language = models.IntegerField()
    reg_Maths = models.IntegerField()
    reg_Science = models.IntegerField()
    reg_Social = models.IntegerField()
    reg_Total = models.IntegerField()

    def __str__(self):
        return self.reg_name