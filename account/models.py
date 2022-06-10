from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# from villa.models import Image, Medium


class VerificationCode(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True,null=False,blank=False)
    vc_code = models.CharField(max_length=6,null=False,blank=False)
    time_generated = models.DateTimeField(auto_now_add=True,null=False,blank=False)

    def __str__(self):
        return self.email + ", Code: " + self.vc_code


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        #user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.first_name = 'admin'
        user.last_name = 'admin'
        user.role = 'superuser'
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # required fields
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20,null=False,blank=False)
    last_name = models.CharField(max_length=40,null=False,blank=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True,null=False,blank=False)
    phone_number = models.CharField(max_length=13, unique=True,null=False,blank=False)
    password = models.CharField(max_length=200, null=False,blank=False)
    role = models.CharField(default='normal-user', max_length=20, verbose_name='role')
    balance = models.FloatField(default=0.0)

    # optional fields
    national_code = models.CharField(max_length=10, unique=True, null=False,blank=False)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    # auto-generate fields
    #username = models.CharField(verbose_name='username', max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Medium(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ImageField(upload_to='villas/medium/',null=False,blank=False)

    class Meta:
        abstract = True


class Document(Medium):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=False,blank=False)
    type = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return f"Document ID: {self.id}, Owner: {self.user.first_name} {self.user.last_name}"


class Image(Medium):
    title = models.CharField(max_length=40, null=True, blank=True)
    width = models.IntegerField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    default = models.BooleanField(default=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f"Image ID: {self.id}, Title: {self.title}"


class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20,null=False,blank=False)
    text = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.text


class Villa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,null=False,blank=False)
    TYPE_CHOICES = [
        ('Coastal', 'Coastal'),
        ('Urban', 'Urban'),
        ('Wild', 'Wild'),
        ('Mountainous', 'Mountainous'),
        ('Desert', 'Desert'),
        ('Rural', 'Rural'),
        ('Suburban', 'Suburban'),
        ('Motel', 'Motel'),
    ]
    type = models.CharField(max_length=12, choices=TYPE_CHOICES,null=False,blank=False)
    description = models.TextField(blank=True, null=True)
    price_per_night = models.IntegerField(null=False,blank=False)
    country = models.CharField(max_length=100,null=False,blank=False)
    state = models.CharField(max_length=100,null=False,blank=False)
    city = models.CharField(max_length=100,null=False,blank=False)
    address = models.TextField(null=False,blank=False)
    postal_code = models.CharField(max_length=10, unique=True,null=False,blank=False)
    latitude = models.FloatField(null=False,blank=False)
    longitude = models.FloatField(null=False,blank=False)
    area = models.IntegerField(null=False,blank=False)
    owner = models.ForeignKey(Account, related_name='villa', on_delete=models.CASCADE,null=False,blank=False)
    capacity = models.IntegerField(null=False,blank=False)
    max_capacity = models.IntegerField(null=False,blank=False)
    number_of_bathrooms = models.IntegerField(default=1)
    number_of_bedrooms = models.IntegerField(default=1)
    number_of_single_beds = models.IntegerField(default=1)
    number_of_double_beds = models.IntegerField(default=1)
    number_of_showers = models.IntegerField(default=1)
    visible = models.BooleanField(default=True)
    rate = models.FloatField(default=3)
    no_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ", Owner: " + self.owner.first_name + " " + self.owner.last_name


class VillaDetail(models.Model):
    id = models.AutoField(primary_key=True)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE,null=False,blank=False)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.id


class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE,null=False,blank=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.id


class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Account, on_delete=models.CASCADE,null=False,blank=False)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE,null=False,blank=False)
    start_date = models.DateField(null=False,blank=False)
    end_date = models.DateField(null=False,blank=False)
    num_of_passengers = models.IntegerField(default=1)
    total_cost = models.FloatField(default=0)
    closed = models.BooleanField(default=False)
    RATE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    rate = models.IntegerField(choices=RATE_CHOICES, null=True,blank=True)

    def __str__(self):
        return self.villa.name + ", Customer: " + self.customer.__str__()
