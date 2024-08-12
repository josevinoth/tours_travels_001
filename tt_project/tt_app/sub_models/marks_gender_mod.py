from django.db import models
# from ..models import Product_info,Department_info,MyUser,Location_info,Vendor_info,Insurance_Info,UnitInfo

class gender_info(models.Model):
    reg_gender_1 = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.reg_gender