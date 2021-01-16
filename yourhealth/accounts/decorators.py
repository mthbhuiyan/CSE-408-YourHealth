from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from .models import Role


def additional_info_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='accounts:add_additional_info'):
    '''
    Decorator for views that checks that the logged in user is has added additional info,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.has_profile,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def doctor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=settings.LOGIN_URL):
    '''
    Decorator for views that checks that the logged in user is a doctor,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_doctor(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
