from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.

def homepage(request):
    return render(request,"Office/HomePage.html")

def my_pro(request):
    data=tbl_office.objects.get(id=request.session["oid"])
    return render(request,"Office/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_office.objects.get(id=request.session["oid"])
    if request.method=="POST":
        prodata.office_name=request.POST.get('txtname')
        prodata.office_contact=request.POST.get('txtcon')
        prodata.office_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Office/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Office/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_office.objects.filter(id=request.session["oid"],office_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_office.objects.get(id=request.session["oid"],office_password=request.POST.get('txtcurpass'))
                userdata.office_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Office/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Office/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Office/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Office/ChangePassword.html")
    

def POSTComplaint(request):
    data=tbl_complaint.objects.filter(office=request.session["oid"])
    userID=tbl_office.objects.get(id=request.session["oid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,office=userID)
        return redirect("Office:POSTComplaint")
    else:
        return render(request,"Office/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("Office:POSTComplaint")

def myrequest(request):
    myreq = tbl_servicerequest.objects.filter(office=request.session["oid"])
    return render(request,"Office/Request.html",{"service":myreq})

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Office/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_office.objects.get(id=request.session["oid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),office_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Office/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_office.objects.get(id=request.session["oid"])
    chat_data = tbl_chat.objects.filter((Q(office_from=user) | Q(office_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Office/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(office_from=request.session["oid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(office_to=request.session["oid"]))).delete()
    return render(request,"Office/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})