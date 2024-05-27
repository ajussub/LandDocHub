from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    
    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),

    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),

    path('SearchOffice/',views.SearchOffice,name='SearchOffice'),
    path('SendRequesttoOffice/<int:id>',views.SendRequesttoOffice,name="SendRequesttoOffice"),
   
    path('ajaxservice/',views.ajaxservice,name="ajaxservice"),
    path('myrequest/',views.myrequest,name="myrequest"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('rateing/<int:mid>',views.rateing,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('calculater/',views.calculater,name="calculater"),

    path('SellingListLandRegistration/',views.SellingListLandRegistration,name="SellingListLandRegistration"),
    path('ajaxplace/',views.ajax_place,name="AjaxPlace"),

    path('SellingLandListNew/',views.SellingLandListNew,name="SellingLandListNew"),
    path('acceptland/<int:aid>',views.acceptland,name="acceptland"),
    path('rejectland/<int:rid>',views.rejectland,name="rejectland"),
    path('LandListAccepted/',views.LandListAccepted,name="LandListAccepted"),
    path('LandListRejected/',views.LandListRejected,name="LandListRejected"),

    path('SearchSellingLandList/',views.SearchSellingLandList,name="SearchSellingLandList"),

    path('KnowledeRepository/',views.KnowledeRepository,name="KnowledeRepository"),

]