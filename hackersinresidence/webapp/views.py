# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    ''' Homepage
    '''
    return render(request, 'pages/index.html')

def opportunities(request):
    ''' Opportunities
    '''
    return render(request, 'pages/opportunities.html')
