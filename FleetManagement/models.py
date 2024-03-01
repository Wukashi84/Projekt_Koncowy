from django.db import models

# Model przedstawiający pojazd


class Uzytkownik:
    pass


class Pojazd:
    pass


class Pojazd(models.Model):
    id = models.AutoField(primary_key=True)
    marka_pojazdu = models.CharField(max_length=255)
    model_pojazdu = models.CharField(max_length=255, blank=True, null=True)
    RODZAJE_POJAZDOW_CHOICES = [
        ('osobowy', 'Osobowy'),
        ('dostawczy', 'Dostawczy'),
        ('ciężarowy', 'Ciężarowy'),
        ('naczepa', 'Naczepa'),
        ('przyczepa', 'Przyczepa'),
    ]
    rodzaj_pojazdu = models.CharField(max_length=255, choices=RODZAJE_POJAZDOW_CHOICES)
    nr_rejestracyjny = models.CharField(max_length=20)
    nr_vin = models.CharField(max_length=17)
    rok_wytworzenia = models.CharField(max_length=4)
    rok_pierwszej_rejestracji = models.DateField(default="2000-01-01")
    moc = models.FloatField(default=0)
    poj_silnika = models.FloatField()
    PALIWO_CHOICES = [
        ('ON', 'Olej napędowy'),
        ('PB', 'Benzyna'),
    ]
    paliwo = models.CharField(max_length=2, choices=PALIWO_CHOICES)
    karta_paliwowa = models.ForeignKey('Karta_paliwowa', on_delete=models.CASCADE, null=True, blank=True)
    uzytkownik = models.OneToOneField('Uzytkownik', on_delete=models.CASCADE, null=True, blank=True, related_name='pojazd_relation')

    def __str__(self):
        return self.marka_pojazdu


class Warsztat(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255)
    adres_ulica = models.CharField(max_length=255)
    adres_miasto = models.CharField(max_length=255)
    adres_kod_pocztowy = models.CharField(max_length=20)
    nip = models.CharField(max_length=10)
    regon = models.CharField(max_length=9)
    telefon = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    www = models.CharField(max_length=255)
    osoba_kontaktowa = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa
class Uzytkownik(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    stanowisko = models.CharField(max_length=255)
    nr_rej_samochodu = models.CharField(max_length=20)
    MPK_CHOICES = [
        (2000, '2000- KOSZTY POŚREDNIE PRODUKCJI'),
        (2100, '2100- KOSZTY UTRZYMANIA RUCHU'),
        (2200, '2200-KOSZTY NADZORU PRODUKCYJNEGO'),
        (2210, '2210-KOSZTY GŁÓWNEGO SPAWALNIKA'),
        (2230, '2230-KOSZTY WŁASNYCH SZKOLEŃ I PRAKTYK'),
        (3300, '3300-KOSZTY NARZĘDZIOWNI'),
        (4000, '4000-KOSZTY DZIAŁU KONTROLI WEWNĘTRZNEJ'),
        (5100, '5100-DYREKTOR DS.HANDLOWYCH'),
        (5110, '5110-KOSZTY DZIAŁU OFERTOWEGO'),
        (5120, '5120-KOSZTY DZIAŁU HANDLOWEGO'),
        (5200, '5200-KOSZTY DZIAŁU ZAKUPOW'),
        (5300, '5300-KOSZTY DZIALU MARKETINGU'),
        (5400, '5400-KOSZTY GOSPOD.MATER., LOGISTYKI I SPEDYCJI'),
        (6100, '6100-DYREKTOR DS. PRODUKCJI, DS. PRZYGOT.I REALIZ.PRODU'),
        (6110, '6110-KOSZTY DZIAŁU PRODUKCJI'),
        (6120, '6120-KOSZTY DZIAŁU PRZYGOTOWANIA'),
        (6130, '6130-KOSZTY DZIAŁU REALIZACJI'),
        (6200, '6200-KOSZTY DZIAŁU PLANOWANIA I CYFRYZACJI'),
        (6300, '6300-KOSZTY DZIAŁU TECHNICZNEGO'),
        (6410, '6410-KOSZTY DZIALU MONTAZOWEGO'),
        (6500, '6500-KOSZTY LABORATORIUM'),
        (6510, '6510-KOSZTY DZIAŁU KONTROLI JAKOŚCI'),
        (6520, '6520-KOSZTY DZIALU ZAPEWN.JAKOŚCI, BHP I OCHRONY ś'),
        (6600, '6600-KOSZTY DZIAŁU INWESTYCJI'),
        (6700, '6700-KOSZTY Z-CY DYREKTORA DS. TECHNOLOGII'),
        (7000, '7000-KOSZTY RADY NADZORCZEJ'),
        (7100, '7100-KOSZTY ZARZĄDU'),
        (7110, '7110-KOSZTY BIURA ZARZĄDU'),
        (7120, '7120-KOSZTY DORADCÓW ZARZADU'),
        (7300, '7300-KOSZTY OBSŁUGI PRAWNEJ'),
        (7310, '7310-KOSZTY DZIAŁU UMÓW'),
        (7400, '7400-KOSZTY DZIAŁU FINANSOWO - KSIĘGOWEGO'),
        (7510, '7510-KOSZTY DZIAŁU KONTROLINGU'),
        (7600, '7600-KOSZTY WYDZIALU ADMINISTRACYJNEGO'),
        (7700, '7700-KOSZTY DZIAŁU INFORMATYKI'),
        (7800, '7800-KOSZTY DZIAŁU PŁAC I ZZL'),
    ]
    mpk = models.IntegerField(choices=MPK_CHOICES)
    pojazd = models.OneToOneField('Pojazd', on_delete=models.CASCADE, null=True, blank=True, related_name='uzytkownik_relation')

    def __str__(self):
        return self.nazwisko

class TowarzystwoUbezpieczeniowe(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa_Towarzystwa = models.CharField(max_length=255)
    adres_ulica = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa_Towarzystwa


class Karta_paliwowa(models.Model):
    id = models.AutoField(primary_key=True)
    nr_karty = models.CharField(max_length=20)
    nr_rejestracyjny = models.CharField(max_length=20)
    data_ważności = models.DateField()
    kod_pin = models.CharField(max_length=4)
    TYP_KARTY_CHOICES = [
        ('KIEROWCA', 'Kierowca'),
        ('SAMOCHOD', 'Samochód'),
    ]
    typ_karty = models.CharField(max_length=50, choices=TYP_KARTY_CHOICES, null=True, blank=True)
    STATUS_CHOICES = [
        ('AKTYWNA', 'Aktywna'),
        ('ZABLOKOWANA', 'Zablokowana'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    LIMIT_CHOICES = [
        ('C_3/60+120', 'C_3/60+120'),
        ('C_3/60+120+AutoGaz', 'C_3/60+120+AutoGaz'),
        ('C_1/75+120', 'C_1/75+120'),
        ('C_1/600+120', 'C_1/600+120'),
    ]
    limit = models.CharField(max_length=50, choices=LIMIT_CHOICES,null=True, blank=True)

    def __str__(self):
        return self.nr_karty
