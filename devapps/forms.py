'''
Created on 30-Nov-2015

@author: harishhr
'''
from django import forms
from django.forms.models import ModelForm
from models import Project_data


class request_form(forms.Form):
        
        CHOICES=[(' t2_small','t2.small (1 vCPU, 2GB Memory)'),
                 ('t2_medium','t2.medium (2 vCPU, 4GB Memory)'),
                 ('m3_medium','m3.medium ( 1 vCPU, 3.74 GB Memory)'),
                 ('yours_choice','other')]
        
      
          
        stackoption=[(' Development','Development'),
                     ('QA','QA'),
                     ('Stage','Stage'),
                     ('Production','Production')]
        s3backetoption=[(True,'Yes'),
                        (False,'No')]
         
        project_Name = forms.CharField(max_length=100)
        instance_type = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
        storage = forms.CharField(max_length=100)
        customer = forms.CharField(max_length=100)
        stack = forms.MultipleChoiceField(choices=stackoption, widget =  forms.CheckboxSelectMultiple)
        specification = forms.CharField(widget=forms.Textarea)
        s3backet =forms.ChoiceField(choices=s3backetoption,widget=forms.RadioSelect())
        server_access =forms.ChoiceField(choices=s3backetoption,widget=forms.RadioSelect())
        db_access =forms.ChoiceField(choices=s3backetoption,widget=forms.RadioSelect())
        summary = forms.CharField(widget=forms.Textarea)
        application_url = forms.URLField()
        database_url = forms.URLField()
        testing_url = forms.URLField()


class Project_list(ModelForm):
    class Meta:
        model = Project_data
        fields = ['instance_name','region','instance_id','instance_state','instance_ip','instance_type','application_url','database_url','testing_url']

        