from korisnik import unos_korisnika
from kategorija import unos_kategorije
from artikl import unos_artikla

korisnici = []
broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, broj_korisnika+1):
    korisnik = unos_korisnika(i)
    korisnici.append(korisnik)

kategorije = []
broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, broj_kategorija+1):
    kategorija = unos_kategorije(i)
    kategorije.append(kategorija)
