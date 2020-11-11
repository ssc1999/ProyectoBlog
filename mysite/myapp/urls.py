from django.urls import path

from . import views

urlpatterns = [
        path ('', views.index, name = 'main'),
        path ('index.html', views.index, name ='index'),
        path ('scripts.html', views.scripts, name ='scripts'),
        path ('start_to.html', views.start_to, name ='start_to'),
        path ('contact.html', views.contact, name ='contact'),
        


]


                