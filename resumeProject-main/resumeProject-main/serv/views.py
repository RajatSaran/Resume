from django.shortcuts import render

# Create your views here.
def services(request):
    context ={'serv':'active'}
    return render(request, 'serv/services.html', context)

    