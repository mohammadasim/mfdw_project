from django.contrib import admin

from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    """
    A class to modify the appearance of Quote form in the admin section of the site.
    """
    # The list of fields to be displayed when a list of all quotes is shown in admin page
    list_display = ('id', 'name', 'company',
                    'submitted', 'quotedate', 'quoteprice')
    # The filters that django will create, that can be used to filter all the quotes when
    # all the submitted quotes are show in the admin section of the app
    list_filter = ('submitted', 'quotedate')
    # readonly makes this field unchangeable in the admin section, the admin can only read this field
    readonly_fields = ('submitted',)
    # fieldsets change the appearance of the quote form in admin section. The first part of each field set defines
    # the name of the field set and the second part contains the form fields that it groups together. If the name is
    # set to None that field set will not become a group.
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'description')
        }),
        ('contact Information', {
            'classes': ('collapse',),
            'fields': ('position', 'company',
                       'address', 'phone', 'web')
        }),
        ('Job Information', {
            'classes': ('collapse',),
            'fields': ('sitesstatus', 'priority', 'jobfile', 'submitted')
        }),
        ('Quote Admin', {
            'classes': ('collapse',),
            'fields': ('quotedate', 'quoteprice', 'username')
        })
    )


admin.site.register(Quote, QuoteAdmin)
