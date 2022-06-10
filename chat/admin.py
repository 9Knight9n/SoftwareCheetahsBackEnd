from django.contrib import admin

# Register your models here.
from .models import *


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat', 'owner', 'text', 'time']
    search_fields = ['text']
    list_filter = ['chat']

    class Meta:
        model = Message


admin.site.register(Message, MessageAdmin)


class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'account1', 'account2']

    class Meta:
        model = Chat


admin.site.register(Chat, ChatAdmin)
