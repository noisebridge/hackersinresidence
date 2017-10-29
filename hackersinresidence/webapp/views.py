# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import messages

from .forms import OpportunityForm

def index(request):
    ''' Homepage
    '''
    return render(request, 'pages/index.html')

def opportunities(request):
    ''' View opportunities
    '''

    return render(request, 'pages/opportunities.html')


def view_opportunity(request):
    ''' show a single opportunity view

    Components of this view are  used for admin to review an opportunity
    It is possible this view will just be totally recycled but linked from 
        an admin view in django admin with admin only decorator or whatever

    HOWEVER - an admin must be able to toggle the opportunity approved

    I think I have written some stuff on managing opportunity state in the past
    Look this stuff up, states like: under_review, approved, expired, spam
    '''

    # will need to pass the opportunity in to be filled in the template
    return render(request, 'pages/view_opportunity.html')


def create_opportunity(request):
    ''' View for an organization create a new opportunity.

    NEXT STEPS:
        Need to add bootstrap to flash message in template
        Try to convert your flask flash context for this?
        review the template first and consider, manual may be better
        but we will need the flash messaging everywhere


    '''

    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Success! Opportunity submitted for review.')
            return HttpResponseRedirect('/create_opportunity/')
    
    # not POST
    else:
        form = OpportunityForm()

    return render(request, 'pages/create_opportunity.html', {'form': form})
