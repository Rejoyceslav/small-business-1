from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Materialy, Uslugi


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def oferta_View(request):
    return render(request, 'oferta.html')


def przeglad_View(request):
    return render(request, 'przeglad.html')


def remonty_View(request):
    return render(request, 'remonty.html')


def sprzedaz_urzadzen_View(request):
    return render(request, 'sprzedaz_urzadzen.html')


def materialy_i_czesci_View(request):
    return render(request, 'materialy_i_czesci.html')


class MaterialyList(ListView):
    model = Materialy
    context_object_name = 'materialy'
    template_name = 'materialy_i_czesci.html'

    def get_context_data(self, **kwargs):
        qs = Materialy.objects.all()

        context = super(MaterialyList, self).get_context_data(**kwargs)
        context['materialy'] = qs
        return context


class UslugiList(ListView):
    model = Uslugi
    context_object_name = 'uslugi'
    template_name = 'materialy_i_czesci.html'

    def get_context_data(self, **kwargs):
        qs = Materialy.objects.all()

        context = super(UslugiList, self).get_context_data(**kwargs)
        context['materialy'] = qs
        return context


def kontakt_View(request):
    return render(request, 'kontakt.html')
