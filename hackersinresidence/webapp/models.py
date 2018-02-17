# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# hopefully the right User object!
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    '''
    file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    from: https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.FileField
    '''
    # the 'test' needs changed to the actual user
    # this is tied to the User as ForeignKey too
    return 'user_{0}/{1}'.format('test', filename)


class Organization(models.Model):
    ''' The base class for describing organizations.
    
    ***
    this class should probably be metadata on the user object
    ***

    FUTURE:
    What other fields would an organization want to define themselves with?

    '''
    # make a relationship on user per organization, allow user to have mult orgs in model
    # but do not code feature into ux components - leave possibility open
    # this cascades by default, but I put it so it is explicit
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=256, blank=False, null=True)
    long_description = models.TextField(null=True)
    link_to_organization = models.TextField(null=True)
    location_city = models.TextField(null=True)
    location_country = models.TextField(null=True)
    slug = models.SlugField(default=None, unique=True, allow_unicode=True, null=True)
    # see user_directory_path function above, upload_to calls this with (instance, filename)
    organization_banner = models.ImageField(upload_to=user_directory_path, default=None)


class Opportunity(models.Model):
    ''' The base class for describing opportunities, consumed in forms.
    
    This class is consumed when a org is making a new opportunity and 
    again when the moderators approve the opportunity.

    The approval template should be the same as the view template that 
    is visible publicly.

    FUTURE:
        - expiration date
        - organization
    '''
    class Meta:
        verbose_name_plural = 'Opportunities'

    # make a organization relationship, orgs should be users
    #organization =  models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)

    # this cascades by default, but I put it so it is explicit
    org_owner = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=256, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True) 
    location_city = models.TextField(null=True)
    location_country = models.TextField(null=True)
 
    ##############
    # below sections are pasted directly from Rich
    ##############

    
    offer_travel_checkbox = models.BooleanField(default=False)
    offer_travel_detail = models.CharField(max_length=256, blank=True, null=True)

    offer_housing_checkbox = models.BooleanField(default=False)
    offer_housing_detail = models.CharField(max_length=256, blank=True, null=True)

    offer_food_checkbox = models.BooleanField(default=False)
    offer_food_detail = models.CharField(max_length=256, blank=True, null=True)

    offer_stipend_checkbox = models.BooleanField(default=False)
    offer_stipend_detail = models.CharField(max_length=256, blank=True, null=True)

    offer_studio_checkbox = models.BooleanField(default=False)
    offer_studio_detail = models.CharField(max_length=256, blank=True, null=True)

    offer_tools_checkbox = models.BooleanField(default=False)
    offer_tools_detail = models.CharField(max_length=256, blank=True, null=True)

    offer_additional_detail = models.TextField(blank=True, null=True)

    require_language = models.CharField(max_length=256, blank=True, null=True)

    require_start_date = models.DateField(blank=True, null=True, help_text="Earliest date the residency can start")
    require_end_date = models.DateField(blank=True, null=True, help_text="Latest date the residency can end")
    require_minimum_stay = models.CharField(max_length=256, blank=True, null=True, help_text="Minimum required length of stay")
    require_maximum_stay = models.CharField(max_length=256, blank=True, null=True, help_text="Minimum required length of stay")
    require_date_detail = models.TextField(blank=True, null=True)

    require_mentoring_checkbox = models.BooleanField(default=False)
    require_mentoring_detail = models.CharField(max_length=256, blank=True, null=True)

    require_talk_checkbox = models.BooleanField(default=False)
    require_talk_detail = models.CharField(max_length=256, blank=True, null=True)

    require_workshop_checkbox = models.BooleanField(default=False)
    require_workshop_detail = models.CharField(max_length=256, blank=True, null=True)

    require_presentation_checkbox = models.BooleanField(default=False)
    require_presentation_detail = models.CharField(max_length=256, blank=True, null=True)

    require_class_checkbox = models.BooleanField(default=False)
    require_class_detail = models.CharField(max_length=256, blank=True, null=True)

    require_hackathon_checkbox = models.BooleanField(default=False)
    require_hackathon_detail = models.CharField(max_length=256, blank=True, null=True)

    require_other_requirements = models.TextField(blank=True, null=True)
