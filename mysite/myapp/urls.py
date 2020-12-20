from django.urls import path

from . import views

urlpatterns = [
        path ('', views.index, name = 'main'),
        path ('index.html', views.index, name ='index'),
        path ('category/<int:category_id>/', views.category, name ='category'),
        path ('script/<int:script_id>/', views.script, name ='script'),
]


                