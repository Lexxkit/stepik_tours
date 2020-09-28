from django.shortcuts import render
from django.http import Http404

from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        if not departure:
            raise Http404
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        if not id:
            raise Http404
        return render(request, 'tours/tour.html')
