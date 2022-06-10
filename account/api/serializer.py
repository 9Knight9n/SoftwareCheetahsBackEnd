from rest_framework import serializers
from account.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'role', 'currency']

    def save(self):
        role = ''
        if 'role' not in self.validated_data:
            role = 'normal-user'

        account = Account(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
            role=role,
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account


class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number',
                  'gender', 'national_code', 'image', 'role', 'bio','birthday', 'currency']


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'


class VillaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villa
        fields = '__all__'


class VillaSearchSerializer(serializers.ModelSerializer):
    default_image_url = serializers.SerializerMethodField('get_default_image')

    class Meta:
        model = Villa
        fields = ['villa_id', 'owner', 'name', 'country', 'state', 'city',
                  'price_per_night', 'latitude', 'longitude', 'default_image_url', 'rate']

    def get_default_image(self, villa):
        images = villa.images
        for i in images.all():
            if i.default:
                return i.image.url



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = ['start_date', 'end_date']


class MyCalendarSerializer(serializers.ModelSerializer):
    villa = VillaSerializer(read_only=True)

    class Meta:
        model = Calendar
        fields = ['calendar_id', 'villa', 'start_date', 'end_date']


class RegisterVillaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = '__all__'

