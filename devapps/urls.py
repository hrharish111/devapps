'''
Created on 09-Nov-2015

@author: harishhr
'''

from django.conf.urls import url,patterns
from django.views.generic import TemplateView
from . import views

# from devapps.views import Project_list

urlpatterns = patterns(
    '',
url(r'home_page',views.Home_page,name="home_page"),
url(r'user_info',views.user_info,name="user_info"),


# url(r'server_conformation',views.Server_conformation, name="server_conformation"),
# url(r'awslist',views.Awslist,name = "awslist"),


url(r'^userdetails/$',views.user_details,name = "userdetails"),
url(r'^create_my_form',views.Create_my_form,name="create_my_form"),
url(r'existinglist',views.existance_list,name = "existinglist"),
url(r'^projectview',views.Project_view,name = "projectview"),
url(r'^projectsave',views.Project_save,name = "projectsave")



)