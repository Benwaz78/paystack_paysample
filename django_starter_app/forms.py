from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
	name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
	address = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))

	class Meta():
		model = Purchase
		fields = '__all__'