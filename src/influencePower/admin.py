from django.contrib import admin
from influencePower import models

admin.site.register(models.Influencer)
admin.site.register(models.NormalUser)
admin.site.register(models.Comment)