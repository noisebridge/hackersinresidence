# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import messages

from .models import Opportunity
from .forms import OpportunityForm

def index(request):
    ''' Homepage
    '''
    return render(request, 'pages/index.html')


def lipsum(request):
    ''' Default page template... simple demo of full column

    This should continue to exist, but should be fleshed out with 
    a major demo of the bootstrap grid and various capabilities.

    If there is javascript, it can show all those features too.
    '''
    return render(request, 'pages/lipsum.html')


def opportunities(request):
    ''' View list of opportunities

    Two functions:
    1. show a filterable list of opportunities
    2. show a user their opportunities (filter by them) with an edit button
        - should accept optional argument of user id or something
        - when the user logs in they should be redirected to this page
        - there should be a login link on the homepage
    '''
    opportunity_list = Opportunity.objects.all()

    return render(request, 'pages/opportunities.html', {'opportunity_list': opportunity_list})


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

    # will need to pass the opportunity in to be filled in the template
    return render(request, 'pages/view_opportunity.html', {'opportunity': opportunity})


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
        form = OpportunityForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Success! Opportunity submitted for review.')
            form.save()

        # if POST and not valid, drop back to regular view
    
    # not POST
    else:
        form = OpportunityForm()

    return render(request, 'pages/create_opportunity.html', {'form': form})
