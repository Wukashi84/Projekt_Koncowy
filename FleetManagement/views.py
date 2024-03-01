from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from reportlab.pdfgen import canvas
from weasyprint import HTML

from .models import Pojazd, Karta_paliwowa, Uzytkownik
from .forms import PojazdForm, Karta_PaliwowaForm, WarsztatForm, TowarzystwoUbezpieczenioweForm, UzytkownikForm


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class DodajPojazdView(View):
    def get(self, request):
        form = PojazdForm()
        return render(request, 'dodaj_pojazd.html', {'form': form})

    def post(self, request):
        form = PojazdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pojazdow')
        return render(request, 'dodaj_pojazd.html', {'form': form})


class UsunPojazdView(View):
    template_name = 'usun_pojazd.html'  # Twój szablon HTML do potwierdzenia usunięcia

    def get(self, request, pk):
        pojazd = get_object_or_404(Pojazd, pk=pk)
        return render(request, self.template_name, {'pojazd': pojazd})

    def post(self, request, pk):
        pojazd = get_object_or_404(Pojazd, pk=pk)
        pojazd.delete()
        return redirect('lista_pojazdow')  # Przekieruj gdziekolwiek po usunięciu, np. do listy pojazdów



class EdytujPojazdView(View):
    def get(self, request, pk):
        pojazd = get_object_or_404(Pojazd, pk=pk)
        form = PojazdForm(instance=pojazd)
        users = Uzytkownik.objects.all()
        return render(request, 'edytuj_pojazd.html', {'pojazd': pojazd, 'form': form, 'users': users})

    def post(self, request, pk):
        pojazd = get_object_or_404(Pojazd, pk=pk)
        form = PojazdForm(request.POST, instance=pojazd)

        # Ręczne przypisanie użytkownika
        user_id = request.POST.get('uzytkownik')
        if user_id:
            user = Uzytkownik.objects.get(pk=user_id)
            pojazd.uzytkownik = user

        if form.is_valid():
            form.save()
            return redirect('lista_pojazdow')

        users = Uzytkownik.objects.all()
        return render(request, 'edytuj_pojazd.html', {'pojazd': pojazd, 'form': form, 'users': users})


class ListaPojazdowView(View):
    def get(self, request):
        # Pobierz wszystkie pojazdy
        pojazdy = Pojazd.objects.all()

        # Dla każdego pojazdu, znajdź kartę paliwową na podstawie numeru rejestracyjnego
        for pojazd in pojazdy:
            try:
                # Znajdź kartę paliwową na podstawie numeru rejestracyjnego
                karta_paliwowa = Karta_paliwowa.objects.get(nr_rejestracyjny=pojazd.nr_rejestracyjny)

                # Przypisz karta_paliwowa do pojazdu
                pojazd.karta_paliwowa = karta_paliwowa
            except Karta_paliwowa.DoesNotExist:
                # Obsłuż sytuację, gdy karta paliwowa nie istnieje
                pojazd.karta_paliwowa = None

        # Zwróć render z danymi pojazdów
        return render(request, 'lista_pojazdow.html', {'pojazdy': pojazdy})


class SzczegolyPojazduView(View):
    def get(self, request, pk):
        pojazd = get_object_or_404(Pojazd, pk=pk)
        return render(request, 'szczegoly_pojazdu.html', {'pojazd': pojazd})


class DodajKarteView(View):
    template_name = 'dodaj_karte.html'

    def get(self, request):
        form = Karta_PaliwowaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Karta_PaliwowaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_kart')  # Przekieruj na stronę z listą kart
        return render(request, self.template_name, {'form': form})

class ListaKart(View):
    def get(self, request):
        karty = Karta_paliwowa.objects.all()
        return render(request, 'lista_kart.html', {'karty': karty})


class SzczegolyKartyView(View):
    template_name = 'szczegoly_karty.html'

    def get(self, request, pk):
        karta = get_object_or_404(Karta_paliwowa, id=pk)
        return render(request, self.template_name, {'karta': karta})


class Karta_Paliwowa:
    pass


class EdytujKarteView(View):
    template_name = 'edytuj_karte.html'

    def get(self, request, pk):
        karta = get_object_or_404(Karta_paliwowa, id=pk)
        form = Karta_PaliwowaForm(instance=karta)
        return render(request, self.template_name, {'form': form, 'karta': karta, 'karta_edited': False})

    def post(self, request, pk):
        karta = get_object_or_404(Karta_paliwowa, id=pk)  # Use 'id=pk' to get the correct object
        form = Karta_PaliwowaForm(request.POST, instance=karta)

        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'karta': karta, 'karta_edited': True})
        else:
            return render(request, self.template_name, {'form': form, 'karta': karta, 'karta_edited': False})

class UsunKarteView(View):
    template_name = 'usun_karte.html'

    def post(self, request, pk):
        karta = get_object_or_404(Karta_paliwowa, pk=pk)
        karta.delete()

        # Dodaj komunikat pomyślnego usunięcia karty
        messages.success(request, 'Karta została pomyślnie usunięta.')

        return redirect('lista_kart')


# Operacje wykonywane na Użytkownikach
class DodajUzytkownikaView(View):
    template_name = 'dodaj_uzytkownika.html'

    def get(self, request):
        form = UzytkownikForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UzytkownikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_uzytkownikow')
        return render(request, self.template_name, {'form': form})


class ListaUzytkownikowView(View):
    def get(self, request):
        uzytkownicy = Uzytkownik.objects.select_related('pojazd').all()
        return render(request, 'lista_uzytkownikow.html', {'uzytkownicy': uzytkownicy})

class EdytowanieUzytkownikaView(View):
    model = Uzytkownik
    form_class = UzytkownikForm
    template_name = 'uzytkownik_form.html'
    success_url = reverse_lazy('lista_uzytkownikow')

class UsuwanieUzytkownikaView(View):
    model = Uzytkownik
    template_name = 'uzytkownik_confirm_delete.html'
    success_url = reverse_lazy('lista_uzytkownikow')

class SzczegolyUzytkownikaView(View):
    template_name = 'szczegoly_uzytkownika.html'

    def get(self, request, pk):
        uzytkownik = get_object_or_404(Uzytkownik, id=pk)
        pojazd = Pojazd.objects.filter(nr_rejestracyjny=uzytkownik.nr_rej_samochodu).first()
        return render(request, self.template_name, {'uzytkownik': uzytkownik, 'pojazd': pojazd})
    
    
class RaportPDF(View):
    def get(self, request, pk, *args, **kwargs):
        # Pobierz odpowiedni pojazd z bazy danych
        pojazd = Pojazd.objects.get(pk=pk)

        # Wczytaj szablon HTML
        template = get_template('raport_pdf_template.html')
        context = {'pojazd': pojazd}
        html_content = template.render(context)

        # Utwórz plik PDF przy użyciu weasyprint
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="raport_pojazdu_{pojazd.id}.pdf"'
        HTML(string=html_content).write_pdf(response)

        return response