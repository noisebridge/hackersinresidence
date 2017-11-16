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

    # upload_to yields instance, filename, see implementation above
    organization_banner = models.FileField(upload_to=user_directory_path, default=None)


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
    # this cascades by default, but I put it so it is explicit
    org_owner = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=256, blank=False, null=True)
    description = models.TextField(null=True)
    expiration_date = models.DateField(null=True) 




