from django.shortcuts import render

# Create your views here.
def clients_all(request):
    return render(request , 'view_all.html')


def add_clients(request):
    return render(request , 'add_clients.html')




