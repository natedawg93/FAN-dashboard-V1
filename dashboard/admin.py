from django.contrib import admin

from .models import Campus, Location, Button

class ButtonAdmin(admin.ModelAdmin):
    list_display = ('name','campus','button_id')

    def campus(self,obj):
        return obj.location.campus

admin.site.register(Campus)
admin.site.register(Location)
admin.site.register(Button, ButtonAdmin)
