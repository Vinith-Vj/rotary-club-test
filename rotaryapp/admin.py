from django.contrib import admin
from .models import History, homeCoverImage, Contact, Membership, Sponsor, Uyare, Event, EventImage, Visitor

# Register your models here.
admin.site.register(homeCoverImage)
admin.site.register(History)
admin.site.register(Contact)
admin.site.register(Membership)
admin.site.register(Sponsor)
admin.site.register(Uyare)

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1  # Number of empty image forms to display

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)

admin.site.register(Visitor)