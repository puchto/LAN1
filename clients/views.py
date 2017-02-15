from django.shortcuts import render
from clients.models import Auth_record
from django.shortcuts import render, get_object_or_404

# Create your views here.

def clients_list(request):
	clients_active = Auth_record.objects.filter(kl_service = 0).order_by('cl_address')
	return render(request, 'clients/clients_list.html', {'clients': clients_active})
	
	
def client_mod(request, pk):
	client = get_object_or_404(Auth_record, pk=pk)
	return render(request, 'clients/client_mod.html', {'client': client})
