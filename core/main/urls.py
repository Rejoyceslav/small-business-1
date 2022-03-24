from . import views
from django.urls import path
from .views import MaterialyList, KontaktView

urlpatterns = [
    path('', views.index, name='index'),
    path('oferta/', views.oferta_View, name='oferta'),
    path('uslugi/', views.uslugi_View, name='uslugi'),
    path('przeglad/', views.przeglad_View, name='przeglad'),
    path('remonty/', views.remonty_View, name='remonty'),
    path('sprzedaz_urzadzen/', views.sprzedaz_urzadzen_View, name='sprzedaz_urzadzen'),
    # path('sprzedaz_urzadzen/', MaterialyList.as_view(), name='sprzedaz_urzadzen'),
    # path('materialy_i_czesci/', views.materialy_i_czesci_View, name='materialy_i_czesci'),
    path('materialy_i_czesci/', MaterialyList.as_view(), name='materialy_i_czesci'),
    # path('kontakt/', views.kontakt_View, name='kontakt'),
    path('kontakt/', KontaktView.as_view(), name='kontakt'),
]
