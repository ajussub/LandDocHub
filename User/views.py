from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Admin.models import *
from django.db.models import Q
from datetime import datetime
import json
from django.http import JsonResponse


def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")
    

def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")


def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("User:UserFeedback")
    else:
        return render(request,"User/UserFeedback.html",{"data":data})
   

def delFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:UserFeedback")



def SearchOffice(request):
    disdata=tbl_district.objects.all()
    officedata=tbl_office.objects.all()


    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    for o in officedata:
        wdata=tbl_office.objects.get(id=o.id)
        tot=0
        ratecount=tbl_rating.objects.filter(office=wdata).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(office=wdata)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
    # print(parry)
    data = zip(officedata,parry)

    if request.method=="POST":
        placeID = tbl_place.objects.get(id=request.POST.get('sel_place'))
        officedata=tbl_office.objects.filter(place=placeID)
        return render(request,"User/SearchOffice.html",{"disdata":disdata,"officedata":officedata})
    else:
         return render(request,"User/SearchOffice.html",{"disdata":disdata,"officedata":officedata,"data":data})
    
def SendRequesttoOffice(request,id):
    officeData=tbl_office.objects.get(id=id)
    serviceData=tbl_services.objects.all()
    if request.method=="POST":
        serviceID = tbl_services.objects.get(id=request.POST.get('selServiceType'))
        userID=tbl_user.objects.get(id=request.session["uid"])
        tbl_servicerequest.objects.create(
            request_message=request.POST.get('txtrequest'),
            service=serviceID,
            user=userID,
            office=officeData
            )
        return redirect('User:homepage')
    else:
        return render (request,"User/SendRequesttoOffice.html",{'officeData':officeData,'serviceData':serviceData})  

def ajaxservice(request):
    service = tbl_services.objects.get(id=request.GET.get("sid"))
    return render(request,"User/AjaxService.html",{"service":service})

def myrequest(request):
    myreq = tbl_servicerequest.objects.filter(user=request.session["uid"])
    return render(request,"User/MyRequest.html",{"service":myreq})


def chatpage(request,id):
    user  = tbl_office.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_user = tbl_office.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,office_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(office_from=tid) | Q(office_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(office_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(office_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def rateing(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    counts=0
    counts=stardata=tbl_rating.objects.filter(office=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(office=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_office.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,office=wdata)
    stardata=tbl_rating.objects.filter(office=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    rate = tbl_rating.objects.filter(office=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(office=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + ratecount
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)

def calculater(request):
    return render(request,"User/Calculater.html")


def SellingListLandRegistration(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        from_user = tbl_user.objects.get(id=request.session["uid"])
        tbl_sellingland.objects.create(
            land_location=request.POST.get('txtlocation'),
            land_contact=request.POST.get('txtcontact'),
            land_landmark=request.POST.get('txtlandmark'),
            land_address=request.POST.get('txt_address'),
            place=place,
            user=from_user,
            land_landimage=request.FILES.get('fileLandImage'),
            land_proof=request.FILES.get('fileLandProof'),
            )

        return redirect('User:SellingListLandRegistration')
    else:
        return render(request,'User/SellingListLandRegistration.html',{'distkey':disdata})
    

def ajax_place(request):
    disid=tbl_district.objects.get(id=request.GET.get('DIST'))
    places=tbl_place.objects.filter(district=disid)
    return render(request,"User/AjaxPlace.html",{'plckey':places})      



def SellingLandListNew(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_sellingland.objects.filter(land_status=0,user=from_user)
    return render(request,"User/SellingLandListNew.html",{"userdata":userdata})

def acceptland(request,aid):
    user = tbl_sellingland.objects.get(id=aid)
    user.land_status = 1
    user.save()
    return redirect("User:homepage")

def rejectland(request,rid):
    user = tbl_sellingland.objects.get(id=rid)
    user.land_status = 2
    user.save()
    return redirect("User:homepage")

def LandListAccepted(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_sellingland.objects.filter(land_status=1,user=from_user)
    return render(request,"User/LandListAccepted.html",{"userdata":userdata})

def LandListRejected(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_sellingland.objects.filter(land_status=2,user=from_user)
    return render(request,"User/LandListRejected.html",{"userdata":userdata})      

def SearchSellingLandList(request):
    userdata = tbl_sellingland.objects.filter(land_status=1)
    return render(request,"User/SearchSellingLandList.html",{"userdata":userdata})



def KnowledeRepository(request):
    serviceData=tbl_knowlederepository.objects.all()
    return render(request,'User/KnowledegeRepositoryView.html',{'serviceData':serviceData}) 
