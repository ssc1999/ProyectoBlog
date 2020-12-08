from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ContactForm
from .models import Contact, Info, Script, Category
from . import views

def index (request) :
    info =Info.objects.latest('id')
    category = get_list_or_404(Category.objects.order_by('number'))
    context = {
        'info' : info,
        'categoryList' : category
    }
    return render(request, "index.html", context)

def category (request, category_id) :
    info =Info.objects.latest('id')
    script =get_list_or_404(Script.objects.order_by('date'), pk=category_id)
    context = {
        'info' : info ,
        'scriptList' : script
    }
    return render(request, "category.html", context)

def script (request, script_id):
    info =Info.objects.latest('id')
    script =get_object_or_404(Script, pk=script_id)
    context = {
        'info' : info ,
        'script' : script
    }
    
    return render(request, "script.html", context)

def contact (request) :
    form = ContactForm()
    info = Info.objects.latest('id')
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





