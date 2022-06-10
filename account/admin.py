import datetime

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import *
from persiantools.jdatetime import JalaliDateTime


class AccountAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2', 'role',
                       'national_code', 'gender', 'birthday', 'image', 'bio',)}),)
    list_display = ('id', 'first_name', 'last_name', 'email', 'get_date_joined', 'role', 'is_admin')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role',)
    exclude = ('password',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    fieldsets = ()

    def get_date_joined(self, obj):
        timestamp = datetime.datetime.timestamp(obj.date_joined)
        jalali_datetime = JalaliDateTime.fromtimestamp(timestamp)
        return jalali_datetime.strftime("%Y/%m/%d - %H:%M")


admin.site.register(Account, AccountAdmin)


class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'vc_code', 'time_generated']
    search_fields = ['email']

    class Meta:
        model = VerificationCode

    def get_time_generated(self, obj):
        timestamp = datetime.datetime.timestamp(obj.time_generated)
        jalali_datetime = JalaliDateTime.fromtimestamp(timestamp)
        return jalali_datetime.strftime("%Y/%m/%d - %H:%M")


admin.site.register(VerificationCode, VerificationCodeAdmin)


# Register your models here.
class VillaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'country', 'city', 'get_owner', 'visible']
    search_fields = ['name', 'country', 'city']
    list_filter = ['type']

    def get_owner(self, obj):
        result = Villa.objects.get(villa_id=obj.id)
        return result.owner.first_name + ' ' + result.owner.last_name

    class Meta:
        model = Villa


admin.site.register(Villa, VillaAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_villa', 'default']
    search_fields = ['title']
    list_filter = ['default']

    def get_villa(self, obj):
        result = Villa.objects.get(images__image_id=obj.id)
        return result.__str__()

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = Document


admin.site.register(Document, DocumentAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    search_fields = ['type']

    class Meta:
        model = Detail


admin.site.register(Detail, DetailAdmin)


class CalendarAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'villa', 'start_date', 'end_date', 'closed']
    list_filter = ['villa']

    class Meta:
        model = Calendar


admin.site.register(Calendar, CalendarAdmin)
