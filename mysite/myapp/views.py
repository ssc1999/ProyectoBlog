from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ContactForm
from .models import Contact, Info
from . import views

def index (request) :
    info = get_object_or_404(Info, pk = 1)
    context = {
        'info' : info 
    }
    return render(request, "index.html", context)

def scripts (request) :
    info = get_object_or_404(Info, pk = 1)
    context = {
        'info' : info 
    }
    return render(request, "scripts.html", context)

def start_to (request) :
    info = get_object_or_404(Info, pk = 1)
    context = {
        'info' : info 
    }
    return render(request, "start_to.html", context)

def contact (request) :
    form = ContactForm()
    info = get_object_or_404(Info, pk = 1)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacto = Contact()
            contacto.name = form.cleaned_data["name"]
            contacto.mail = form.cleaned_data["mail"]
            contacto.subject = form.cleaned_data["subject"]
            contacto.message = form.cleaned_data["message"]
            contacto.save()
        return HttpResponseRedirect(reverse(views.contact))
    context = {
        'form' : form,
        'info' : info
    }
    return render(request, "contact.html", context)





