from django.urls import path,include
from Admin import views

app_name="webadmin"

urlpatterns = [

    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('district/',views.district,name="district"),
    path('deldis/<int:id>',views.deldis,name="deldis"),
    path('editdis/<int:eid>',views.editdis,name="editdis"),


    path('place/',views.place,name="place"),
    path('delplace/<int:id>',views.delplace,name="delplace"),

    path('type/',views.type,name="type"),
    path('deltype/<int:id>',views.deltype,name="deltype"),
    path('edittype/<int:id>',views.edittype,name="edittype"),

    path('serviceRegistration/',views.serviceRegistration,name="serviceRegistration"),
    path('delService/<int:id>',views.delService,name="delService"),
    
    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
    path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),

    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),
    
    path('OfficeListNew/',views.OfficeListNew,name="OfficeListNew"),
    path('acceptoffice/<int:aid>',views.acceptoffice,name="acceptoffice"),
    path('rejectoffice/<int:rid>',views.rejectoffice,name="rejectoffice"),
    path('OfficeListAccepted/',views.OfficeListAccepted,name="OfficeListAccepted"),
    path('OfficeListRejected/',views.OfficeListRejected,name="OfficeListRejected"),

    path('ComplaintListNew/',views.ComplaintListNew,name="ComplaintListNew"),
    path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
    path('ComplaintSolved/',views.ComplaintSolved,name="ComplaintSolved"),


    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),

    path('KnowledeRepository/',views.KnowledeRepository,name="KnowledeRepository"),
    path('delKnowrepo/<int:id>',views.delKnowrepo,name="delKnowrepo"),
    
    
  
]
