from django.db import models
# from ..models import Product_info,Department_info,MyUser,Location_info,Vendor_info,Insurance_Info,UnitInfo

class registration_info(models.Model):
    reg_name = models.CharField(max_length=50,blank=True)
    reg_age = models.IntegerField()
    reg_mobile_no = models.IntegerField()

    def __str__(self):
        return self.reg_name