from django.shortcuts import render

# Create your views here.

def clients_list(request):
    return render(request, 'clients/clients_list.html', {})
