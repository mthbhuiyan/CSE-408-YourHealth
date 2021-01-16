from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    PATIENT = 1
    DOCTOR = 2
    DELIVERYMAN = 3
    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (DELIVERYMAN, 'Deliveryman'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    has_profile = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def is_doctor(self):
        return self.roles.filter(id=Role.DOCTOR).exists()


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField()


class Doctor(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default=False)
    degree = models.CharField(max_length=50)
    institute = models.CharField(max_length=100)


class Location(models.Model):
    address = models.CharField(max_length=150)
    

class Deliveryman(models.Model):
    deliveryman = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_assigned = models.BooleanField(default=False)
    addresses = models.ManyToManyField(Location, blank=True)
