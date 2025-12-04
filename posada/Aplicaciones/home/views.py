from django.shortcuts import render

def home_view(request):
    """
    Vista principal que sirve como Dashboard para acceder a las funcionalidades.
    """
    return render(request, 'home.html')
