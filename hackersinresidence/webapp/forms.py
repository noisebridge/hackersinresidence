from django import forms

from .models import Opportunity, Organization

from django.utils.text import slugify

class OpportunityForm(forms.ModelForm):
    ''' Django form describing the Opportunity model

    Available Form Fields: https://docs.djangoproject.com/en/1.11/ref/forms/fields/
    '''
    class Meta:
        model = Opportunity
        fields = ['title', 'description', 'expiration_date', 'offer_travel_checkbox', 'offer_travel_detail', 'offer_housing_checkbox', 'offer_housing_detail', 'offer_food_checkbox', 'offer_food_detail', 'offer_stipend_checkbox', 'offer_stipend_detail', 'offer_studio_checkbox', 'offer_studio_detail', 'offer_tools_checkbox', 'offer_tools_detail', 'offer_additional_detail', 'require_language', 'require_start_date', 'require_end_date', 'require_minimum_stay', 'require_maximum_stay', 'require_date_detail', 'require_mentoring_checkbox', 'require_mentoring_detail', 'require_talk_checkbox', 'require_talk_detail', 'require_workshop_checkbox', 'require_workshop_detail', 'require_presentation_checkbox', 'require_presentation_detail', 'require_class_checkbox', 'require_class_detail', 'require_hackathon_checkbox', 'require_hackathon_detail', 'require_other_requirements']

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control'}),
                'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

                'application_instructions': forms.TextInput(attrs={'class': 'form-control'}),
    
                'offer_travel_checkbox': forms.CheckboxInput(),
                'offer_travel_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'offer_housing_checkbox': forms.CheckboxInput(),
                'offer_housing_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'offer_food_checkbox': forms.CheckboxInput(),
                'offer_food_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'offer_stipend_checkbox': forms.CheckboxInput(),
                'offer_stipend_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'offer_studio_checkbox': forms.CheckboxInput(),
                'offer_studio_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'offer_tools_checkbox': forms.CheckboxInput(),
                'offer_tools_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'offer_additional_detail': forms.Textarea(attrs={'class': 'form-control'}),

                'require_language': forms.TextInput(attrs={'class': 'form-control'}),

                'require_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'require_end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'require_minimum_stay': forms.TextInput(attrs={'class': 'form-control'}),
                'require_maximum_stay': forms.TextInput(attrs={'class': 'form-control'}),
                'require_date_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_mentoring_checkbox': forms.CheckboxInput(),
                'require_mentoring_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_talk_checkbox': forms.CheckboxInput(),
                'require_talk_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_workshop_checkbox': forms.CheckboxInput(),
                'require_workshop_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_presentation_checkbox': forms.CheckboxInput(),
                'require_presentation_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_class_checkbox': forms.CheckboxInput(),
                'require_class_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_hackathon_checkbox': forms.CheckboxInput(),
                'require_hackathon_detail': forms.TextInput(attrs={'class': 'form-control'}),

                'require_other_requirements': forms.Textarea(attrs={'class': 'form-control'}),
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
