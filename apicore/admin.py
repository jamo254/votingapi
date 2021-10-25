from django.contrib import admin
from apicore.models import*
# Register your models here.
#Регистрация моделей

    
admin.site.register(Question)
admin.site.register(Choice)


class DateAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('start_date')
        else:
            return []
