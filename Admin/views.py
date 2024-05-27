from django.shortcuts import render,redirect
from Admin.models import *
from datetime import date
from Guest.models import *
from User.models import *
def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")

def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get('district'))
        return render(request,'Admin/District.html',{"districtkey":dis})
    else:
        return render(request,'Admin/District.html',{"districtkey":dis})


def deldis(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("webadmin:district")


def editdis(request,eid):
    dis=tbl_district.objects.all()
    disdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        disdata.district_name=request.POST.get('district')
        disdata.save()
        return redirect("webadmin:district") 
    else:  
          return render (request,"Admin/district.html",{'disdata':disdata,"districtkey":dis})   
          

def place(request):
    disob=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(
            place_name=request.POST.get('txtplace'),
            place_pincode=request.POST.get('txtnum'),
            district=dis)
        return render(request,'Admin/place.html',{"placedata":place,'disob':disob})
    else:
        return render(request,'Admin/place.html',{"placedata":place,'disob':disob})

def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("webadmin:place")               



def type(request):
    typedata=tbl_type.objects.all()
    if request.method=="POST":
        tbl_type.objects.create(type_name=request.POST.get('type_name'))
        return render(request,'Admin/type.html',{"typekey":typedata})
    else:
        return render(request,'Admin/type.html',{"typekey":typedata})

def deltype(request,id):
    tbl_type.objects.get(id=id).delete()
    return redirect("webadmin:type")    

def edittype(request,id):
    typedata=tbl_type.objects.get(id=id)
    if request.method=="POST":
        typedata.type_name=request.POST.get('type_name')
        typedata.save()
        return redirect("webadmin:type") 
    else:  
          return render (request,"Admin/type.html",{'typedata':typedata})             


def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return redirect("webadmin:adminInsertSelect")
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("webadmin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("webadmin:adminInsertSelect")
    else:
        return render(request,"Admin\AdminRegistration.html",{"editdata":editdata})


        
        
def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("webadmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})      




def OfficeListNew(request):
    officedata = tbl_office.objects.filter(office_status=0)
    return render(request,"Admin/OfficeListNew.html",{"officedata":officedata})

def acceptoffice(request,aid):
   office = tbl_office.objects.get(id=aid)
   office.office_status = 1
   office.save()
   return redirect("webadmin:LoadingHomePage")

def rejectoffice(request,rid):
   office = tbl_office.objects.get(id=rid)
   office.office_status = 2
   office.save()
   return redirect("webadmin:LoadingHomePage")

def OfficeListAccepted(request):
   officedata = tbl_office.objects.filter(office_status=1)
   return render(request,"Admin/OfficeListAccepted.html",{"officedata": officedata})

def OfficeListRejected(request):
    officedata = tbl_office.objects.filter(office_status=2)
    return render(request,"Admin/OfficeListRejected.html",{"officedata":officedata})      


def ComplaintListNew(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    officedata=tbl_office.objects.all()
    officeComplaint=tbl_complaint.objects.filter(complaint_status=0,office__in=officedata)
    return render(request,"Admin/ComplaintListNew.html",{'userComplaint':userComplaint,'officeComplaint':officeComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("webadmin:LoadingHomePage")
    else:
        return render(request,"Admin/ComplaintListReply.html",{'complaint':complaint})
    
def ComplaintSolved(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    officedata=tbl_office.objects.all()
    officeComplaint=tbl_complaint.objects.filter(complaint_status=1,office__in=officedata)
    return render(request,"Admin/ComplaintListSolved.html",{'userComplaint':userComplaint,'officeComplaint':officeComplaint})

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Admin/UserFeedBack.html",{'data':data})


def serviceRegistration(request):
    serviceData=tbl_services.objects.all()
    if request.method=="POST" and request.FILES:
        tbl_services.objects.create(
            services_title=request.POST.get('txttilte'),
            services_details=request.POST.get('txtdetails'),
            services_criteria=request.POST.get('txtcriteria'),
            services_document=request.FILES.get('fileDocs'),
            )

        return redirect('webadmin:serviceRegistration')
    else:
        return render(request,'Admin/Services.html',{'serviceData':serviceData})    
    
def delService(request,did):
    tbl_services.objects.get(id=did).delete()
    return redirect("webadmin:serviceRegistration")




def KnowledeRepository(request):
    serviceData=tbl_knowlederepository.objects.all()
    if request.method=="POST" and request.FILES:
        tbl_knowlederepository.objects.create(
            knowrepo_title=request.POST.get('txttilte'),
            knowrepo_details=request.POST.get('txtdetails'),
            knowrepo_document=request.FILES.get('fileDocs'),
            )

        return redirect('webadmin:KnowledeRepository')
    else:
        return render(request,'Admin/KnowledeRepository.html',{'serviceData':serviceData})    
    
def delKnowrepo(request,id):
    tbl_knowlederepository.objects.get(id=id).delete()
    return redirect("webadmin:KnowledeRepository")