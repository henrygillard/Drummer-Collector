from django.contrib import admin
from .models import Drum, Drummer, Sponsor
# Register your models here.
admin.site.register(Drummer)
admin.site.register(Sponsor)
admin.site.register(Drum)

