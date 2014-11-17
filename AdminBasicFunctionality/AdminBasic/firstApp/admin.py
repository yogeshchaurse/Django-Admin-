from django.contrib import admin
from django.db import models
from . import models

# Register your models here Once you register your model here
#  it will give you default CRUD operations for your registered models

class ClientIndustryAdmin(admin.ModelAdmin):

    #Set search_fields to enable a search box on the admin change list page.
    # This should be set to a list of field names that will be searched
    # whenever somebody submits a search query in that text box.

    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )

class ClientAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'industry__name',
    )

    list_display = (
        'name',
        'industry',
        'mailing_city',
        'mailing_zip',
        'website',
    )


admin.site.register(models.ClientIndustry, ClientIndustryAdmin)
admin.site.register(models.Client, ClientAdmin)