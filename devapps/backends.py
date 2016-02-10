'''
Created on 28-Nov-2015

@author: harishhr
'''
from django.contrib.auth.models import User

class ClientAuthBackend(object):
    
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            return user
            if password == User.objects.get(password=password):
                return user
            else:
                return None
            
        except Exception as e:
            return None
        
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
            