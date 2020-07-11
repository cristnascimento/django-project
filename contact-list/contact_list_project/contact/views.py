from django.shortcuts import render, redirect
from .services import ContactService
from .mock_data import Contact

service = ContactService()

def index(request):
    return render(request, 'contact/home.html')

def list(request):
    contacts = service.getContacts()
    data = {"contacts": contacts}
    return render(request, 'contact/list.html', data)

def add(request):
    data = { "mode": "add", "action": "/contact/post", "readonly": "", "disabled": "", "contact": Contact()}
    return render(request, 'contact/contact.html', data)

def edit(request, id):
    contact = service.getContact(id)
    data = { "mode": "edit",  "action": "/contact/update/"+str(id), "readonly": "", "disabled": "", "contact": contact}
    return render(request, 'contact/contact.html', data)

def view(request, id):
    contact = service.getContact(id)
    data = { "mode": "view",  "action": "", "readonly": "readonly", "disabled": "disabled", "contact": contact}
    return render(request, 'contact/contact.html', data)

def post(request):
    contact = Contact()
    contact.setFromForm(request)
    service.createContact(contact)
    return redirect("/contact/list")

def update(request, id):
    contact = Contact()
    contact.setFromForm(request)
    contact.id = id
    service.updateContact(contact)
    return redirect("/contact/view/"+str(id))

def delete(request, id):
    service.deleteContact(id)
    return redirect("/contact/list")