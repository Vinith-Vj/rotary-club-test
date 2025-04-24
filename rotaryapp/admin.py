from django.contrib import admin
from .models import History, homeCoverImage, Contact, Membership, Sponsor, Uyare

# Register your models here.
admin.site.register(homeCoverImage)
admin.site.register(History)
admin.site.register(Contact)
admin.site.register(Membership)
admin.site.register(Sponsor)
admin.site.register(Uyare)

