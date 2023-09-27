from django.contrib import admin
from .models import Group, Message
# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = "name",
    
@admin.register(Message)
class Messagedmin(admin.ModelAdmin):
    list_display = ['content']