from django.contrib import admin
from django.db.models.constraints import CheckConstraint

# Register your models here.
from .models import Mdactorcategory,Mdassettypes,Mdcastatus,Mddimensions,Mddrivertypes,Mdgeneralscale,Mdmanagementmethods,Mdoccurrences,Mdorgtypes,Mdphases,Mdstakes,Mdstatus,Missions,Contributionstasks,Dispensationrecords,Orgdeliverables,Orggoals,Orgmilestones,Assodimimp,Assodso,Assomilestonesdispen,Assomissiondrivers,Assostakeholderdso,Assostakeholderdsocontribution
admin.site.register(Mdactorcategory),
admin.site.register(Mdassettypes),
admin.site.register(Mdcastatus),
admin.site.register(Mddimensions),
admin.site.register(Mddrivertypes),
admin.site.register(Mdgeneralscale),
admin.site.register(Mdmanagementmethods),
admin.site.register(Mdoccurrences),
admin.site.register(Mdorgtypes),
admin.site.register(Mdphases),
admin.site.register(Mdstakes),
admin.site.register(Mdstatus),
admin.site.register(Missions),
admin.site.register(Contributionstasks),
admin.site.register(Dispensationrecords),
admin.site.register(Orgdeliverables),
admin.site.register(Orggoals),
admin.site.register(Orgmilestones),
admin.site.register(Assodimimp),
admin.site.register(Assodso),
admin.site.register(Assomilestonesdispen),
admin.site.register(Assomissiondrivers),
admin.site.register(Assostakeholderdso),
admin.site.register(Assostakeholderdsocontribution)