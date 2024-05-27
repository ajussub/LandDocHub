from django.urls import path,include
from Office import views
app_name="Office"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),
    path('myrequest/',views.myrequest,name="myrequest"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
]
