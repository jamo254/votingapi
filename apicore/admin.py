from django.contrib import admin
from apicore.models import*
# Register your models here.
#Регистрация моделей

    
# admin.site.register(Question)
admin.site.register(Choice)

@admin.register(Question)
class DateAdmin(admin.ModelAdmin):
    # ...
    readonly_fields = ['start_date']
    # ...
# 