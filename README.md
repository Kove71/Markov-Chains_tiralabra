# Markov-ketjut tekstin generoimisessa

Tiralabran projekti. Ohjelma generoi tekstiä korpustekstin perusteella käyttämällä markov-ketjua ja trie-datarakennetta.

## Nykyinen versio

Tekstin generointi on implementoitu vapaavalinteisella korpuksella ja markov-ketjun asteella. Tekstin generoimiseen käytetään trie-rakennetta. Testaus ei ole vielä kattavaa. PyQt5 tuottaa ongelmia pylintin kanssa, joten käyttöliittymää ei vielä testata. 

## Käyttöohje

Ennen ensimmäistä käyttökertaa riippuvuudet tulee asentaa komennolla: 
```bash
poetry install
```
Ohjelma suoritetaan komennolla:
```bash
poetry run invoke start
```
Testaus suoritetaan komennolla:
```bash
poetry run invoke test
```
Coverage-report luodaan komennolla:
```bash
poetry run invoke coverage
```
Tämän jälkeen juurihakemistosta löytyy hakemisto htmlcov/, josta voi katsoa raportin.

Trie-tietorakennetta voi testata juurihakemistossa komennolla:
```bash
poetry run python3 src/trie.py
```


## Python-versio

Ohjelma on testattu python-versiolla 3.8.10, mutta kaikki python 3.8.0 korkeammat versiot pitäisi toimia.

## Dokumentaatio

- [Määrittelydokumentti](/Dokumentaatio/maarittelydokumentti.md/)
- [Työaikakirja](Dokumentaatio/tyoaikakirja.md/)
- [Testausdokumentti](Dokumentaatio/testausdokumentti.md)

## Viikkoraportit

- [Viikko 1](/Dokumentaatio/viikkoraportti1.md/)
- [Viikko 2](/Dokumentaatio/viikkoraportti2.md/)
- [Viikko 3](/Dokumentaatio/viikkoraportti3.md/)

