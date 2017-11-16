from django import forms

from .models import Opportunity, Organization

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
                'location' : forms.TextInput(attrs={'class': 'form-control'}),
                }

class OrganizationForm(forms.ModelForm):
    ''' Django form describing the Opportunity model

    Available Form Fields: https://docs.djangoproject.com/en/1.11/ref/forms/fields/
    '''
    class Meta:
        model = Organization 
        fields = ['title', 'long_description', 'link_to_organization', 'location_city', 'location_country', 'organization_banner']
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'long_description': forms.Textarea(attrs={'class': 'form-control'}),
                'link_to_organization': forms.TextInput(attrs={'class': 'form-control'}),
                'location_city': forms.TextInput(attrs={'class': 'form-control'}),
                'location_country': forms.TextInput(attrs={'class': 'form-control'}),
                }
