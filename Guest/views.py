from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

# Create your views here.


def user(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(
            user_name=request.POST.get('txt_name'),
            user_contact=request.POST.get('txt_num'),
            user_email=request.POST.get('txt_email'),
            user_gender=request.POST.get('gender'),
            user_address=request.POST.get('txt_address'),
            place=place,
            user_photo=request.FILES.get('txt_photo'),
            user_proof=request.FILES.get('txt_proof'),
            user_password=request.POST.get('txt_password')
            )

        return redirect('Guest:user')
    else:
        return render(request,'Guest/Userreg.html',{'distkey':disdata})


def ajax_place(request):
    disid=tbl_district.objects.get(id=request.GET.get('DIST'))
    places=tbl_place.objects.filter(district=disid)
    return render(request,"Guest/AjaxPlace.html",{'plckey':places})        


def officeReg(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_office.objects.create(
            office_name=request.POST.get('txt_name'),
            office_contact=request.POST.get('txt_num'),
            office_email=request.POST.get('txt_email'),
            office_address=request.POST.get('txt_address'),
            office_logo=request.FILES.get('txt_photo'),
            office_proof=request.FILES.get('txt_proof'),
            office_password=request.POST.get('txt_password'),
            place=plcid)

        return redirect('Guest:officeReg')
    else:
        return render(request,'Guest/NewOffice.html',{'distkey':disdata})    

        


def login(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_password')
        
        ucount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        admincount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        officecount=tbl_office.objects.filter(office_email=Email,office_password=Password,office_status='1').count()
        if ucount > 0:
            userdata=tbl_user.objects.get(user_email=Email,user_password=Password)
            request.session['uid']=userdata.id
            return redirect('User:homepage')
        elif officecount > 0:
            officedata=tbl_office.objects.get(office_email=Email,office_password=Password)
            request.session['oid']=officedata.id
            return redirect('Office:homepage')
        elif admincount > 0:
            admindata=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session['aid']=admindata.id
            return redirect('webadmin:LoadingHomePage')
        else:
            message="Invalid Credentials!!"
            return render(request,'Guest/login.html',{'msg':message})
    else:
        return render(request,'Guest/login.html')    
    


def Homepage(request):
    return render(request,"Guest/Homepage.html")          




 

