from django.contrib import admin
from .models import Name_Picture


class faceAdmin(admin.ModelAdmin):
    list_display = (
        'picture',
        'names',
    )

    fieldsets = (
        (None, {
            'fields': (
                'names',
                'picture'
            )
        }),
    )

    list_editable = ['names']


admin.site.register(Name_Picture, faceAdmin)
