from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError

from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        # raise 404 if url parameter is incorrect
        if departure not in ['msk', 'spb', 'nsk', 'ekb', 'kzn']:
            raise Http404
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        # raise 404 if url parameter is incorrect
        if id not in range(1, 11):
            raise Http404
        return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Кажется возникли проблемы...')
