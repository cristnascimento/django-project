from django.shortcuts import render

def index(request):
    data = {'name': 'john'}
    return render(request, 'contact/contact.html', data )
