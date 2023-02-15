from django.contrib import admin
from hsm.models import Appointment
# Register your models here.

#admin.site.register(Appointment)
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','date','department','mobile','message']