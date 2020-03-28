from django.contrib import admin
from app import models
# Register your models here.
admin.site.register(models.About)
admin.site.register(models.Comment)
admin.site.register(models.News)
admin.site.register(models.Review)
admin.site.register(models.Service)
admin.site.register(models.Message)
admin.site.register(models.Doctor)
admin.site.register(models.ServicePicture)
