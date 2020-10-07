from random import sample

from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError

from django.views import View

import data


class MainView(View):
    def get(self, request, *args, **kwargs):
        # Choosing 6 random id from tours dictionary
        random_tours_id = sample(data.tours.keys(), 6)
        # Create dictionary with 6 random tours for render at index.html
        random_tours = {idx: data.tours[idx] for idx in random_tours_id}
        context = {'random_tours': random_tours,
                   'title': data.title,
                   'subtitle': data.subtitle,
                   'description': data.description,
                   'departures': data.departures}
        return render(request, 'tours/index.html', context=context)


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        # Raise 404 if url parameter is incorrect
        if departure not in data.departures:
            raise Http404
        # Choosing tours with desired 'departure'
        filtered_tours = {tour_id: tour_info for tour_id, tour_info in data.tours.items()
                          if tour_info['departure'] == departure}
        # Create additional variables for rendering at templates
        departure_name = data.departures[departure]
        prices = [tour['price'] for tour in filtered_tours.values()]
        nights = [tour['nights'] for tour in filtered_tours.values()]

        context = {'filtered_tours': filtered_tours,
                   'departure_name': departure_name,
                   'min_price': min(prices),
                   'max_price': max(prices),
                   'min_nights': min(nights),
                   'max_nights': max(nights),
                   'title': data.title,
                   'departures': data.departures}
        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, tour_id, *args, **kwargs):
        tour = data.tours.get(tour_id)
        # Raise 404 if tour doesn't exist
        if tour is None:
            raise Http404
        # Get departure's full name for rendering in template
        departure_name = data.departures[tour['departure']]

        context = {'tour': tour,
                   'departure_name': departure_name,
                   'departures': data.departures,
                   'title': data.title}
        return render(request, 'tours/tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Кажется такой страницы не существует. Проверьте адрес!')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите, извините!')
