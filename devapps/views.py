from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oauth2client import client
 
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import httplib2
from apiclient import discovery
from devapps.models import Created_form,Project_data
from .forms import request_form,Project_list
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import boto.ec2
import os
from boto.connection import HTTPResponse
clienturl =  os.getcwd()+"/provision/templates/devapps/client_secret_1069477560960-mpicrpqrd0mrahleo8nn40lmrtqpcaus.apps.googleusercontent.com.json"
def Home_page(request):
    flow=client.flow_from_clientsecrets(clienturl,
                                        scope='https://www.googleapis.com/auth/userinfo.email',
                                        redirect_uri='http://localhost:8000/home_page'
                                        )
     
    flow.params['include_granted_scopes']="true"
    flow.params['login_hint']="above-inc.com"
    flow.params['hd'] = "above-inc.com"
    flow.params['access_type'] = 'online'


    if 'code' not in (request.GET.keys()):
        auth_uri = flow.step1_get_authorize_url()
        return HttpResponseRedirect(auth_uri)
          
    else:
        auth_code = request.GET.get('code')
        credentials = flow.step2_exchange(auth_code)
        request.session['credentials'] = credentials.to_json()
        return HttpResponseRedirect(reverse('user_info'))

 
def user_info(request):
    
    if 'credentials' not in request.session:
        return HttpResponseRedirect(reverse('home_page'))
     
    
    credentials = client.OAuth2Credentials.from_json(request.session['credentials'])

     
    if credentials.access_token_expired:
        return HttpResponseRedirect(reverse('home_page'))

    
    http_auth = credentials.authorize(httplib2.Http())
    service = discovery.build('plus', 'v1', http=http_auth)
    google_request = service.people().get(userId='me')
    result = google_request.execute(http=http_auth)
    
    if 'domain' not in result.keys():
        return HttpResponse("Not a valid user to register") 
    
    elif result['domain'] == "above-inc.com":
        email = result['emails'][0]['value']
        username = email[:-14]
        password = result['id']
    else:
        return HttpResponse("Nothing")
    try:
        saved_user = User.objects.get(username = username,password=password,email = email)   
    except Exception as e:
        print e
        saved_user = User(username=username,password=password,email = email)
        saved_user.save()
    
            
    try:    
        user = authenticate(username=saved_user, password=password)
         
    except Exception as e:
        print e
        return HTTPResponse("not authenticated")
    
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('userdetails'))
        else:
            return HttpResponseRedirect(reverse("home_page"))
    else:
        print "some were wrong in else login else"
        return HttpResponseRedirect(reverse("home_page"))    
 
 
 
         
 





@csrf_exempt
@login_required(login_url="user_info")
def Create_my_form(request):
    if request.method =='POST':
        form = request_form(request.POST)
        if form.is_valid():
            project_Name = form.cleaned_data['project_Name']
            instance_type = form.cleaned_data['instance_type']
            storage = form.cleaned_data['storage']
            customer = form.cleaned_data['customer']
            stack = form.cleaned_data['stack']
            specification = form.cleaned_data['specification']
            s3backet = form.cleaned_data['s3backet']
            server_access = form.cleaned_data['server_access']
            db_access = form.cleaned_data['db_access']
            summary = form.cleaned_data['summary']
             
 
            if instance_type == "yours_choice":
                instance_type = request.POST.get('other_reason')
          
            try:
                p = Created_form(user_key=request.user,project_Name=project_Name,instance_type=instance_type,storage=storage,
                                customer=customer,stack=stack,specification=specification,s3backet=s3backet,
                                server_access=server_access,db_access=db_access,summary=summary )
                p.save()
                
            except:
                form = request_form()
                return render(request,'devapps/createrequest.html',{"form":form,"invalid":"Form is invalid"})
            
            try:
                send_mail('server request', 'Thank for the request please wait until the admin review your request', 'harish.hr@above-inc.com',
                          [str(request.user.email)], fail_silently=False)
                 
                recipient_list = User.objects.get(is_superuser=1)
                send_mail('new request', "please click the link below"+ "http:localhost:8000/test", 'harish.hr@above-inc.com', [str(recipient_list.email)])
                return HttpResponseRedirect(reverse('userdetails'))
            except Exception as e:
                return HttpResponse(e)    
             
             
             
        else:
            return HttpResponse("please fill the form")
    else:
        form = request_form()

        return render(request,'devapps/createrequest.html',{"form":form})


@login_required(login_url="user_info")    
def user_details(request):
    user_id =request.user.id
    user_view = Created_form.objects.filter(user_key = user_id)
    return render(request,'devapps/userdata.html',{'userview':user_view})



 
 
@login_required(login_url="user_info")
def existance_list(request,data = None):
    
    region_list = ["ap-southeast-1","us-west-1"]
    access_key = "AKIAJHJBI6HUTHFUD3RA"
    secret_key = "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"

    instance_list = []
    for reg in region_list: 
            ec2_conn = boto.ec2.connect_to_region(reg,
                                              aws_access_key_id = access_key,
                                              aws_secret_access_key=secret_key)
            reservations =  ec2_conn.get_all_instances()
            for reservation in reservations:
                for inst in reservation.instances:
                    
                    instance_each = [inst.tags.get('Name'),reg,inst.id,inst.state,inst.ip_address,inst.instance_type]
                    instance_list.append(instance_each)
                   
    existing_list = instance_list
    
    if data is None:
        data = "" 
    return render(request,'devapps/existinginstance.html',{'existing':existing_list,'data':data})














 
def Project_view(request):
    instance_name = request.GET.get('insname')
    region = request.GET.get('region')
    instance_id = request.GET.get('ins_id')
    instance_state = request.GET.get('ins_state')
    instance_ip = request.GET.get('ins_ip')
    instance_type = request.GET.get('ins_type')
#     application_url = request.GET.get('app_url')
#     database_url = request.GET.get('database_url')
#     testing_url = request.GET.get('testing_url')
     
    try:
        saved_data = Project_data.objects.get(instance_name=instance_name,instance_id=instance_id)
        saved_db = ({"saved_instance":saved_data.instance_name,
                      "saved_region":saved_data.region,
                      "saved_id":saved_data.instance_id,
                      "saved_state":saved_data.instance_state,
                      "saved_ip":saved_data.instance_ip,
                      "saved_type":saved_data.instance_type,
                      "application_url":saved_data.application_url,
                      "database_url":saved_data.database_url,
                      "testing_url":saved_data.testing_url
                      })
        return render(request,'devapps/about.html',{"saved_db":saved_db})
         
    except Exception as e:
        print e
        form = Project_list(initial ={'instance_name':instance_name,'region':region,'instance_id':instance_id,'instance_state':instance_state,'instance_ip':instance_ip,'instance_type':instance_type})
        return render(request,'devapps/projectformview.html',{'data':form})
         
 
 
@csrf_exempt        
def Project_save(request):
    if request.method == 'POST':
        form = Project_list(request.POST)
        if form.is_valid():
            form.save()
            
            data = "Thank you, your request has been saved"
            return existance_list(request,data)
        else:
            data = "Your form is not saved"
            return existance_list(request,data) 
    return HttpResponse("success")
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
# @login_required(login_url="user_info")
# def Server_conformation(request):
#      
#     if request.user.is_staff:
#         return HttpResponse ("ok sir")
#          
#     else:
#         return HttpResponse( "get lost")
#      
#      
#      
#     return HttpResponse("success")
