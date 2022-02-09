from django.db import models
from django.forms import ModelForm
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.mail

class Info(models.Model):
    name = models.CharField(default="Name Error", max_length=20)
    f_nac = models.DateField()
    desc = models.CharField(max_length = 1000)

    def __str__(self):
        return self.desc

class Category(models.Model):
    name = models.CharField(default="Null", max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name

    @property
    def number_of_scripts(self):
        size = Script.objects.filter(category=Category.objects.get(name=self.name)).count()
        return size


class Script(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now)
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='myapp/static/img/script', verbose_name='Image', null = True, blank=True)

    def __str__(self):
        return self.title
