from django.contrib import admin
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from .models import Pojazd, Karta_paliwowa, Warsztat, TowarzystwoUbezpieczeniowe, Uzytkownik


# Dodawanie nowego pojazdu w panelu administracji
@admin.register(Pojazd)
class PojazdAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'marka_pojazdu',
        'model_pojazdu',
        'rodzaj_pojazdu',
        'rok_wytworzenia',
        'nr_rejestracyjny',
        'rok_pierwszej_rejestracji',
        'nr_vin',
        'moc',
        'poj_silnika',
        'paliwo',
    )
    search_fields = (
        'marka_pojazdu',
        'nr_rejestracyjny',
        'rok_produkcji',
        'paliwo',
        'uzytkownik'
    )
    list_display_links = ('marka_pojazdu',)

    actions = ['edycja_pojazdow']

    def edycja_pojazdow(self, request, queryset):
        for pojazd in queryset:
            pojazd.save()
        self.message_user(request, f'Zaktualizowano {queryset.count()} pojazdów.')
        if queryset.exists():
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (pojazd._meta.app_label, pojazd._meta.model_name),
                        args=[queryset.first().id]))

    edycja_pojazdow.short_description = 'Edycja wybranych pojazdów'

@admin.register(Karta_paliwowa)
class Karta_paliwowaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nr_karty',
                    'nr_rejestracyjny',
                    'data_ważności',
                    'kod_pin',
                    'typ_karty',
                    'status',
                    'limit')
    list_display_links = ('nr_karty', 'nr_rejestracyjny')
    search_fields = ('nr_karty',)  # Add this line for searching by card number
    actions = ['edycja_karty']

@admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ('id', 'imie', 'nazwisko', 'stanowisko', 'nr_rej_samochodu', 'mpk')
    list_display_links = ('imie', 'nazwisko')
    search_fields = ('nr_rej_samochodu',)
    actions = ['edycja_uzytkownikow']

