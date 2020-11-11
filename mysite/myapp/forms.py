from django import forms

class ContactForm(forms.Form):
    names = forms.CharField(max_length=100)
    mail = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)