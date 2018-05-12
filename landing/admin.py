from django.contrib import admin
from .models import Sponsor, Quota, Event, About

# Register your models here.
admin.site.register(Quota)
admin.site.register(Sponsor)
admin.site.register(Event)
admin.site.register(About)
