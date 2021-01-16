from django.urls import path
from django.views.generic import TemplateView

from .views import LocationUpdateView


app_name = 'locations'

urlpatterns = [
    path('', TemplateView.as_view(template_name='locations/location_update.html'), name='index'),
    path('update/', LocationUpdateView.as_view(), name='update'),
]
