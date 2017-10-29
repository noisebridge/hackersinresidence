from django import forms


class OpportunityForm(forms.Form):
    ''' Django form describing the Opportunity model

    Available Form Fields: https://docs.djangoproject.com/en/1.11/ref/forms/fields/
    '''
    title = forms.CharField(label="Title", max_length=256)
    description = forms.CharField(label="Description", widget=forms.Textarea)
