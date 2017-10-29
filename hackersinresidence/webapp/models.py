# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Organization(models.Model):
    ''' The base class for describing organizations, 
    
    ***

    this class should probably be metadata on the user object

    ***

    '''
    # do not use yet, read comments
    pass

class Opportunity(models.Model):
    ''' The base class for describing opportunities, consumed in forms.
    
    This class is consumed when a org is making a new opportunity and 
    again when the moderators approve the opportunity.

    The approval template should be the same as the view template that 
    is visible publicly.
    '''
    # make a organization relationship, orgs should be users
    title = models.CharField(max_length=256, blank=False, null=True)
    description = models.TextField(null=True)
     
