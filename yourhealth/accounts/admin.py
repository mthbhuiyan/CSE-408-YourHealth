from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from tempus_dominus.widgets import DatePicker

from .models import User, Role, Profile, Doctor, Activation


class UserCreationForm(BaseUserCreationForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget)
    
    class Meta(BaseUserCreationForm):
        model = User
        fields = '__all__'

class UserChangeForm(BaseUserChangeForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget)

    class Meta(BaseUserChangeForm):
        model = User
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (*BaseUserAdmin.fieldsets , ('New info', {'fields': ('has_profile', 'roles', 'phone_number',)}))
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2')}
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Activation)
admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.unregister(Group)