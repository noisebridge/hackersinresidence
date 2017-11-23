from django import forms

from .models import Opportunity, Organization

from django.utils.text import slugify

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

class OrganizationForm(forms.ModelForm):
    ''' Django form describing the Opportunity model

    Available Form Fields: https://docs.djangoproject.com/en/1.11/ref/forms/fields/
    '''
    class Meta:
        model = Organization 
        fields = ['title', 'slug', 'long_description', 'link_to_organization', 'location_city', 'location_country', 'organization_banner']
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'long_description': forms.Textarea(attrs={'class': 'form-control'}),
                'link_to_organization': forms.TextInput(attrs={'class': 'form-control'}),
                'location_city': forms.TextInput(attrs={'class': 'form-control'}),
                'location_country': forms.TextInput(attrs={'class': 'form-control'}),
                'slug': forms.TextInput(attrs={'class': 'form-control'}),
                'organization_banner': forms.ClearableFileInput(),
                }
        
        # option to auto-construct slug, lets leave it in user/admin hands
        #def save(self):
        #    ''' generate a unique slug on organization creation
        #    from: https://keyerror.com/blog/automatically-generating-unique-slugs-in-django
        #    '''
        #    # UPDATE existing OBJECT: skip generating a slug
        #    if self.instance.pk:
        #        return super(OrganizationForm, self).save()

        #    # NEW OBJECT: add the slug when submitting the new form
        #    instance = super(OrganizationForm, self).save()

        #    # why isn't this just an alias to instance.slug? it creates 2 objects?
        #    instance.slug = orig = slugify(instance.title)

        #    for x in itertools.count(1):
        #        ''' add -1 -2 -3 etc to the slug until it is unique

        #        I don't like the negation here but lets keep it simple.
        #        '''
        #        if not Organization.objects.filter(slug=instance.slug).exists():
        #            # save the slug
        #            break
        #        instance.slug = '{}-{}'.format(orig, x)

        #    instance.save()
        #    return instance
