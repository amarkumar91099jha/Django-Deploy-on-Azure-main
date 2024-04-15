from django.contrib import admin
from .models import Project, BuildingAddress, IndividualCustomerData, ResilianceCustomerData

admin.site.register(Project)
admin.site.register(BuildingAddress)
admin.site.register(IndividualCustomerData)
admin.site.register(ResilianceCustomerData)