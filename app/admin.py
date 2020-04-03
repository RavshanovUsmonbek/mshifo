from django.contrib import admin
from app import models

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.HospitalInfo)
admin.site.register(models.Comment)
admin.site.register(models.ServicePicture)
admin.site.register(models.Doctor)
admin.site.register(models.News)
admin.site.register(models.Review)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.OpeningHour)
admin.site.register(models.Phone)
admin.site.register(models.Contact)
admin.site.register(models.Follower)
admin.site.register(models.Message)
admin.site.register(models.ServiceCategory)




