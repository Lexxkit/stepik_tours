import data


def base_data(request):
    context = {'title': data.title,
               'departures': data.departures}
    return context
