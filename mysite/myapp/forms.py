from django import forms

class ContactForm(forms.Form):
    names = forms.CharField(max_length = 100)
    number = forms.CharField(max_length = 9)
    mail = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)