from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.subject

class Info(models.Model):
    nombre = models.CharField(max_length=100)
    f_nac = models.DateField()
    desc = models.CharField(max_length = 1000)