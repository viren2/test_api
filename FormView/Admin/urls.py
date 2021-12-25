from django.urls import path
from .import views
from .views import  AdminCreate,Adminlist,Detail,Updatedetail,Deletedata

urlpatterns=[
    path('',AdminCreate.as_view()),
    path('viewadmin',Adminlist.as_view()),
    path('finddetail/<pk>/',Detail.as_view()),
    path('<pk>/updatedetail/',Updatedetail.as_view()),
    path('<pk>/deletedata/',Deletedata.as_view())





]