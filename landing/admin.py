from django.contrib import admin
from .models import Sponsor, Quota, Event

# Register your models here.
admin.site.register(Quota)
admin.site.register(Sponsor)
admin.site.register(Event)
