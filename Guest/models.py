from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
   user_name=models.CharField(max_length=50)
   user_contact=models.IntegerField(null=True)
   user_email=models.EmailField(max_length=50)
   user_gender=models.CharField(max_length=50)
   user_address=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   user_photo=models.FileField(upload_to='Assests/UserDocs/')
   user_proof=models.FileField(upload_to='Assests/UserDocs/')
   user_password=models.CharField(max_length=50)
   user_status=models.IntegerField(default=0)


class tbl_office(models.Model):
   office_name=models.CharField(max_length=50)
   office_contact=models.CharField(max_length=50)
   office_email=models.CharField(max_length=50)
   office_address=models.CharField(max_length=50)
   place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
   office_logo=models.FileField(upload_to='Assests/OfficeDocs/')
   office_proof=models.FileField(upload_to='Assests/OfficeDocs/')
   office_password=models.CharField(max_length=50)
   office_status=models.IntegerField(default=0)
   office_doj=models.DateField(auto_now_add=True)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    office_to = models.ForeignKey(tbl_office,on_delete=models.CASCADE,related_name="office_to",null=True)
    office_from = models.ForeignKey(tbl_office,on_delete=models.CASCADE,related_name="office_from",null=True)

