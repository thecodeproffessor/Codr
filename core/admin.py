from django.contrib import admin
from .models import About, Client, RecentWork, Service

# Register your models here.
admin.site.register(About)
admin.site.register(Client)
admin.site.register(RecentWork)
admin.site.register(Service)