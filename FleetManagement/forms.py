from django import forms
from .models import Karta_paliwowa, Pojazd, Warsztat, TowarzystwoUbezpieczeniowe, Uzytkownik


class PojazdForm(forms.ModelForm):
    class Meta:
        model = Pojazd
        fields = '__all__'
        labels = {
            'marka_pojazdu': 'Marka pojazdu',
            'model_pojazdu': 'Model pojazdu',
            'rodzaj_pojazdu': 'Rodzaj pojazdu',
            'nr_rejestracyjny': 'Nr rejestracyjny',
            'rok_produkcji': 'Rok produkcji',
            'rok_pierwszej_rejestracji': 'Rok pierwszej rejestracji',
            'nr_vin': 'Nr VIN',
            'moc': 'Moc',
            'poj_silnika': 'Pojemność silnika',
            'paliwo': 'Paliwo',
            'mpk': 'MPK',
            'uzytkownik': 'Użytkownik',
        }

        widgets = {
            'rok_produkcji': forms.TextInput(attrs={'type': 'date'}),
            'rok_pierwszej_rejestracji': forms.TextInput(attrs={'type': 'date'}),
            # 'mpk': forms.Select(choices=Pojazd.MPK_CHOICES),
            'paliwo': forms.Select(choices=Pojazd.PALIWO_CHOICES),
        }

class Karta_PaliwowaForm(forms.ModelForm):
    class Meta:
        model = Karta_paliwowa
        fields = '__all__'

class WarsztatForm(forms.ModelForm):
    class Meta:
        model = Warsztat
        fields = '__all__'
        labels = {
            'nazwa': 'Nazwa warsztatu',
            'adres_ulica': 'Adres ulica',
            'adres_miasto': 'Adres miasto',
            'adres_kod_pocztowy': 'Adres kod pocztowy',
            'nip': 'NIP',
            'regon': 'REGON',
            'telefon': 'Telefon',
            'email': 'Email',
            'www': 'WWW',
            'osoba_kontaktowa': 'Osoba kontaktowa',
        }

class TowarzystwoUbezpieczenioweForm(forms.ModelForm):
    class Meta:
        model = TowarzystwoUbezpieczeniowe
        fields = '__all__'
        labels = {
            'nazwa_Towarzystwa': 'Nazwa towarzystwa',
            'adres_ulica': 'Adres ulica',
        }

class UzytkownikForm(forms.ModelForm):
    class Meta:
        model = Uzytkownik
        fields = '__all__'
        labels = {
            'imie': 'Imie',
            'nazwisko': 'Nazwisko',
            'stanowisko': 'Stanowisko',
            'nr_rej_samochodu': 'Nr. rej. samochodu',
            'mpk': 'MPK',
        }