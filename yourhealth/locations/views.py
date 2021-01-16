from django.shortcuts import render
from django.http import HttpResponseForbidden, JsonResponse
from django.views import View

from .models import Location


class LocationUpdateView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        if lat is None or lng is None:
            return JsonResponse({'error': 'bad request'}, status=400)
        loc, created = Location.objects.update_or_create(user=request.user, defaults = {'latitude': lat, 'longitude': lng})
        loc.save()
        return JsonResponse({}, status=204)
        
