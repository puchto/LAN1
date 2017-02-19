from django import forms
from django.forms import ModelForm

from clients.models import Auth_record

class Edit_form(forms.ModelForm):

    class Meta:
        model = Auth_record
        fields = ('mac', 'ip_add', 'kl_service', 'downl', 'upl',)
       
       
class Src_form(forms.Form):

	address = forms.CharField()
          
        
