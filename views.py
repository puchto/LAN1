from django.shortcuts import render

def clients_list(request):
    return render(request, 'LAN1/clients_list.html', {})
