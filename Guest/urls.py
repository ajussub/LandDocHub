from django.urls import path,include
from Guest import views

app_name="Guest"

urlpatterns = [

    path('user/',views.user,name="user"),
    path('ajaxplace/',views.ajax_place,name="AjaxPlace"),
    path('officeReg/',views.officeReg,name="officeReg"),   
    path('login/',views.login,name="login"),
    path('',views.Homepage,name="Homepage"),
   
    
]