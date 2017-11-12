from django import forms

from .models import Opportunity

class OpportunityForm(forms.ModelForm):
    ''' Django form describing the Opportunity model

    Available Form Fields: https://docs.djangoproject.com/en/1.11/ref/forms/fields/
    '''
    class Meta:
        model = Opportunity
        fields = ['title', 'description', 'expiration_date']
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control'}),
                'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                }
