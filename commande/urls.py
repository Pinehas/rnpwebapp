from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),


    path('list_cmd', views.list_cmd, name="list_cmd  "),
    path('list_dmd', views.list_dmd, name="list_dmd  "),
    path('insert_cmd', views.insert_cmd, name="insert_cmd  "),
    path('insert_dmd', views.insert_dmd, name="insert_dmd  "),

    path('editcmd/<int:id>/', views.editcmd, name="editcmd"),
    path('updatecmd/<int:id>/', views.updatecmd, name="updatecmd"),
    path('delcmd/<int:id>/', views.delcmd, name="delcmd"),

    path('editdmd/<int:id>/', views.editdmd, name="editdmd"),
    path('updatedmd/<int:id>/', views.updatedmd, name="updatedmd"),
    path('deldmd/<int:id>/', views.deldmd, name="deldmd"),



]
