import datetime
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from.models import Udi, Dollar
from .forms import SearchSeriesForm


def get_min_max_avg(data):
    values = [obj.value for obj in data]
    if len( values) == 0:
        return {'min': 0, 'max': 0, 'avg': 0}
    values.sort()
    try:
        avg = sum(values)/len(values)
    except ZeroDivisionError as e:
        avg = 0
    return {'min': values[0], 'max': values[-1], 'avg': avg}

def index(request):
    """ series view"""
    start_date = datetime.datetime.today() - datetime.timedelta(days=1)
    end_date = datetime.datetime.today()
    if request.method == 'POST':
        print("request.POST", request.POST)
        form = SearchSeriesForm(request.POST)
        print("form", form, dir(form))
        print(form.cleaned_data)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
    # 
    udis = Udi.objects.filter(date__range=[start_date, end_date]).order_by('date')
    udis_stats = get_min_max_avg(udis)
    udis_stats['name'] = _('UDIS')
    udis_stats['data'] = udis
    # dolars
    dollars = Dollar.objects.filter(date__range=[start_date, end_date]).order_by('date')
    dollars_stats = get_min_max_avg(dollars)
    dollars_stats['name'] = _("DOLLARS")
    dollars_stats['data'] = dollars
    context = {
        'series': [
        udis_stats,
        dollars_stats,
        ]
    }
    return render(request, 'index.html', context=context)
