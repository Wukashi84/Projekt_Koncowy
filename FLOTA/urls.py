from django.contrib import admin
from django.urls import path

from FleetManagement.views import DashboardView, DodajPojazdView, ListaPojazdowView, SzczegolyPojazduView, \
    EdytujPojazdView, DodajKarteView, ListaKart, UsunPojazdView, SzczegolyKartyView, EdytujKarteView, UsunKarteView, \
    ListaUzytkownikowView, DodajUzytkownikaView, UsuwanieUzytkownikaView, EdytowanieUzytkownikaView, \
    SzczegolyUzytkownikaView, RaportPDF

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", DashboardView.as_view(), name="dashboard"),
    path("dodaj_pojazd/", DodajPojazdView.as_view(), name="dodaj_pojazd"),
    path("lista_pojazdow/", ListaPojazdowView.as_view(), name="lista_pojazdow"),
    path('szczegoly/<int:pk>/', SzczegolyPojazduView.as_view(), name='szczegoly_pojazdu'),
    path('edytuj_pojazd/<int:pk>/', EdytujPojazdView.as_view(), name='edytuj_pojazd'),
    path('dodaj/', DodajKarteView.as_view(), name='dodaj_karte'),
    path('lista_kart/', ListaKart.as_view(), name='lista_kart'),
    path('usun_pojazd/<int:pk>/', UsunPojazdView.as_view(), name='usun_pojazd'),
    path('szczegoly_karty/<int:pk>/', SzczegolyKartyView.as_view(), name='szczegoly_karty'),
    path('edytuj_karte/<int:pk>/', EdytujKarteView.as_view(), name='edytuj_karte'),
    path('usun_karte/<int:pk>/', UsunKarteView.as_view(), name='usun_karte'),
    path('lista_uzytkownikow/', ListaUzytkownikowView.as_view(), name='lista_uzytkownikow'),
    path('szczegoly_uzytkownika/<int:pk>/', SzczegolyUzytkownikaView.as_view(), name='szczegoly_uzytkownika'),
    path('dodaj_uzytkownika/', DodajUzytkownikaView.as_view(), name='dodaj_uzytkownika'),
    path('edytuj_uzytkownika/<int:pk>/', EdytowanieUzytkownikaView.as_view(), name='edytuj_uzytkownika'),
    path('usun_uzytkownika/<int:pk>/', UsuwanieUzytkownikaView.as_view(), name='usun_uzytkownika'),
    path('generuj_raport_pdf/<int:pk>/', RaportPDF.as_view(), name='generuj_raport_pdf'),

]
