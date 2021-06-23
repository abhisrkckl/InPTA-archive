from django.contrib import admin

from .models import Telescope, Backend, Proposal, Source, DataFormat, Astronomer

# Register your models here.

admin.site.register(Telescope)
admin.site.register(Backend)
admin.site.register(Proposal)
admin.site.register(Source)
admin.site.register(DataFormat)
admin.site.register(Astronomer)
