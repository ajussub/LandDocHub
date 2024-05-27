from django.db import models
from Guest.models import *
# Create your models here.

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
    office=models.ForeignKey(tbl_office, on_delete=models.CASCADE,null=True)
  

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_servicerequest(models.Model):   
    request_date=models.DateField(auto_now_add=True)
    request_message=models.CharField(max_length=500)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
    service=models.ForeignKey(tbl_services, on_delete=models.CASCADE,null=True)
    office=models.ForeignKey(tbl_office, on_delete=models.CASCADE,null=True)
    
class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    office=models.ForeignKey(tbl_office,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)


class tbl_sellingland(models.Model):
   land_location=models.CharField(max_length=50)
   land_contact=models.IntegerField(null=True)
   land_landmark=models.EmailField(max_length=50)
   land_address=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
   land_landimage=models.FileField(upload_to='Assests/LandImage/')
   land_proof=models.FileField(upload_to='Assests/LandProof/')
   land_status=models.IntegerField(default=0)