from django.shortcuts import render
from clients.models import Auth_record

# Create your views here.

def clients_list(request):
	clients_active = Auth_record.objects.filter(kl_service = 0).order_by('cl_address')
	return render(request, 'clients/clients_list.html', {'clients': clients_active})
