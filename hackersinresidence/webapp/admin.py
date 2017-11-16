# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Organization, Opportunity

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    pass

class OpportunityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
