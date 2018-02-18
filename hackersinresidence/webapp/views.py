# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib import messages

from .models import Opportunity, Organization
from .forms import OpportunityForm, OrganizationForm

from django.core.files.uploadedfile import SimpleUploadedFile

from django.core.mail import send_mail
from django.conf import settings

import datetime

def view_404(request):
    ''' 404 page
    '''
    return render(request, 'pages/404.html')

def index(request):
    ''' Homepage
    '''
    return render(request, 'pages/index.html')

def privacy(request):
    ''' Privacy Policy 
    '''
    return render(request, 'pages/privacy.html')

def terms(request):
    ''' Not used, but exists
    '''
    return render(request, 'pages/terms.html')

def contact(request):
    ''' Not used, but exists
    '''
    return render(request, 'pages/contact.html')

def bugs(request):
    ''' Not used, but exists
    '''
    return render(request, 'pages/bugs.html')


def lipsum(request):
    ''' Default page template... simple demo of full column

    This should continue to exist, but should be fleshed out with 
    a major demo of the bootstrap grid and various capabilities.

    If there is javascript, it can show all those features too.
    '''
    return render(request, 'pages/lipsum.html')


def opportunities(request, opportunity_order=''):
    ''' View list of opportunities

    Two functions:
    1. show a filterable list of opportunities
    2. show a user their opportunities (filter by them) with an edit button
        - should accept optional argument of user id or something
        - when the user logs in they should be redirected to this page
        - there should be a login link on the homepage
    '''
    # i can sort the queryset here somehow, by checking what the opportunity suffix will be
    opportunities = Opportunity.objects.all()

    # sort by url-specified order hackersinresidence.org/opportunities/by_description
    # it would be cool, and possible, to allow the sort to be reversed if the user is already on the same page,
    # so that if you are already on by_title, then clicking the "Opportunity" header would reverse the sort...
    if opportunity_order == 'by_expiration':
        opportunities = opportunities.order_by('expiration_date')
    elif opportunity_order == 'by_title':
        opportunities = opportunities.order_by('title')
    elif opportunity_order == 'by_description':
        opportunities = opportunities.order_by('description')
    elif opportunity_order == 'by_org':
        # i think this does a sort by index, not alphabetical. oh well, it's not javascript
        opportunities = opportunities.order_by('org_owner')
    elif opportunity_order == 'by_location':
        opportunities = opportunities.order_by('location_city', 'location_country')

    opportunity_display_list = list()
    for opportunity in opportunities:
        # skip expired, don't skip missing
        if opportunity.expiration_date and opportunity.expiration_date < datetime.date.today():
            continue
        opportunity_link = "/opportunity/{}".format(opportunity.id)
        org = opportunity.org_owner
        org_title = org.title
        org_location = '{city} {country}'.format(city=org.location_city, country=org.location_country)
        opportunity_display = { 'title' : opportunity.title, 'description' : opportunity.description, 'org_title' : org_title, 'org_location' : org_location, 'expiration' : opportunity.expiration_date, 'link': opportunity_link }
        opportunity_display_list.append(opportunity_display)

    return render(request, 'pages/opportunities.html', {'opportunity_display_list': opportunity_display_list })


def view_opportunity(request, opportunity_id):
    ''' show a single opportunity view

    The route for this view is: /opportunity/

    Components of this view are  used for admin to review an opportunity
    It is possible this view will just be totally recycled but linked from 
        an admin view in django admin with admin only decorator or whatever

    HOWEVER - an admin must be able to toggle the opportunity approved

    I think I have written some stuff on managing opportunity state in the past
    Look this stuff up, states like: under_review, approved, expired, spam
    '''
    opportunity = Opportunity.objects.get(pk=opportunity_id)
    organization = opportunity.org_owner

    # will need to pass the opportunity in to be filled in the template
    return render(request, 'pages/view_opportunity.html', {'opportunity': opportunity, 'organization': organization})


def create_opportunity(request):
    ''' View for an organization create a new opportunity.

    NEXT STEPS:
        Get the model populated at this stage
        Send a mail to a mailman listserv when a new opportunity is successfully submitted.


    FUTURE: 
        A version of this view should be used for the "edit opportunity" workflow
        example: https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#modelform

    obviously we do need to store a relationship for opportunity to the user
    then the user can query for all their opportunitys (manage opportunitys view)

    allow a user to edit a opportunity by being its owner and going to its url?
    not sure the UX of this -> how about /edit/ link from a bar at the top that says "edit this opportunity"
    the edit must be APPROVED again by admins, so it just sets its flag to something like 'needs approval'

    ideally users will get an email kicked to them when an admin approves their opportunity, but
    the emailing system we discussed only has one notification email - to the admins on opportunity submission
    however, it isn't so bad to send one to an org when approved, they will have to have an email for login system
    '''

    if request.method == 'POST':
        # necessary to populate organization relationship field based on the user's org.
        # use user.opportunity foreign key to populate relationship

        # user can technically make opportunities before finishing their registration... 
        # this can be prevented in validation or something
        # created - not used yet
        org, created = Organization.objects.get_or_create(user_owner=request.user)

        # we can do a get_or_create() instead here to use this for editing objects
        # we just have to supply the primary key that we want to edit
        opportunity = Opportunity.objects.create(org_owner=org)

        form = OpportunityForm(request.POST, instance=opportunity)
        if form.is_valid():
            messages.success(request, 'Success! Your opportunity will be reviewed within 1-2 days by site moderators. Please check back regularly.')
            form.save()

            mail_subject = 'HIR: Opportunity Review Ready'
            mail_message = 'Hi HIR Admins, \n\n A new HIR Opportunity is ready to be reviewed in the admin area.'
            send_mail(mail_subject, mail_message, settings.EMAIL_HOST_USER, settings.ADMINS)

            # org redirects to the user's org by default (if logged in, which must be the case here)
            return redirect('/org/')

        # if POST and not valid, drop back to regular view
    
    # not POST
    else:
        form = OpportunityForm()

    return render(request, 'pages/create_opportunity.html', {'form': form})


def update_organization(request):
    ''' Update an organization via a form

    This view should be used to update an existing organization.
    The user will PROBABLY have an associated organization on account creation.

    Since this updates an org it will need to grab info for the specific
    object represented by the user going to the update org page.

    The update org page will be a link on the user's landing page.

    User landing page has link to: create_opportunity, update_organization
    User landing page also has a list of opportunities.
    Additionally they will need a delete button which links to a delete
    opportunity page which only has a confirmation button and only
    works for that user.

    Org fields come from the model.
    This will also need to manage processing an image.
    When an organization model is updated, it needs to be approved by admins.
    This email may fire from the view, or use some hook...

    FUTURE:
    - Ideally this can be recycled to create an organization, but currently a single account manages a single organization.
    '''

    # copied/updated from opportunity - make sure to grab the model for the org
    # from the user's organization
    if request.method == 'POST':
        # necessary to populate organization relationship field based on the user's org.
        # use user.opportunity foreign key to populate relationship
        user_organization, created = Organization.objects.get_or_create(user_owner=request.user)
        form = OrganizationForm(request.POST, request.FILES, instance=user_organization)
        if form.is_valid():
            messages.success(request, 'Success! Organization submitted for review.')
            form.save()
            # return to org page, not good to hardcode the url below?
            return redirect('/org/{}/'.format(user_organization.slug))

        # if POST and not valid, drop back to regular view
    
    # not POST
    else:
        user_organization, created = Organization.objects.get_or_create(user_owner=request.user)
        form = OrganizationForm(instance=user_organization)

    return render(request, 'pages/update_organization.html', {'form': form})

def view_organization(request, org_slug=None):
    ''' View an organization's information
    '''
    # should also pull the user from the url if present in the url
    if not org_slug:
        if request.user.is_authenticated:
            organization = Organization.objects.filter(user_owner=request.user).first()
            if organization:
                # not good to hardcode the url below?
                return redirect('/org/{}/'.format(organization.slug))
            else:
                return redirect('update_organization')
        # user is not authenticated yet, log them in
        else:
            return redirect('/account/login/')

    # if org_slug, get the organization
    else:
        organization = get_object_or_404(Organization, slug=org_slug)

    # used to determine whether to show the edit org button in the template
    user_owner = organization.user_owner

    return render(request, 'pages/view_organization.html', { 'organization' : organization, 'user_owner' : user_owner })
