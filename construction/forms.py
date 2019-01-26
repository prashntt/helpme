from django import forms
from django.forms import ModelForm
from construction.models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields='__all__'
		widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
			'Phone_Number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Phone Number'}),
			'Email': forms.TextInput(attrs={'class': 'form-control','placeholder':'E-Mail Address'}),
			'Subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
			'Message': forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Message'}),
        }