# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


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
    #user_owner = 
    title = models.CharField(max_length=256, blank=False, null=True)
    long_description = models.TextField(null=True)
    link_to_organization = models.TextField(null=True)
    location_city = models.TextField(null=True)
    location_country = models.TextField(null=True)


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
    # make a organization relationship, orgs should be users
    #orgaization = 
    title = models.CharField(max_length=256, blank=False, null=True)
    description = models.TextField(null=True)
    expiration_date = models.DateField(null=True) 
