from django.shortcuts import render
from clients.models import Auth_record
from forms import *
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404

# Create your views here.

def main_view(request):
	return render(request, 'clients/main.html')
	
def clients_search(request):
	form = Src_form(request.POST or None)
	if form.is_valid():
		
		
		clients = Auth_record.objects.filter(cl_address__contains = form.cleaned_data['address']).order_by('cl_address')
		return render(request, 'clients/clients_list.html', {'clients': clients})
	return render(request, 'clients/clients_search.html', {'form': form})

def clients_list(request):
	###clients_active = Auth_record.objects.filter(kl_service = 0).order_by('cl_address')
	clients_active = Auth_record.objects.all().order_by('cl_address')
	return render(request, 'clients/clients_list.html', {'clients': clients_active})
	
	
def client_info(request, pk):
	client = get_object_or_404(Auth_record, pk=pk)
	return render(request, 'clients/client_info.html', {'client': client})
	

def client_edit(request, pk):
	client = get_object_or_404(Auth_record, pk=pk)
	form = Edit_form(request.POST or None, instance = client)
	if form.is_valid():
          form.save()
          return redirect('client_info', pk=pk)
	return render(request, 'clients/client_edit.html', {'client': client, 'form': form})
