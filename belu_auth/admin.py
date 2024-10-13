from django.contrib import admin
from .models import BeluUserProfile, BeluUser

admin.site.register(BeluUser)
admin.site.register(BeluUserProfile)
