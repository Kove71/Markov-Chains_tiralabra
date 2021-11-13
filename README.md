# Markov-ketjut tekstin generoimisessa

Tiralabran projekti. Ohjelma generoi tekstiä korpustekstin perusteella käyttämällä markov-ketjua ja trie-datarakennetta.

## Nykyinen versio

Tekstin generoimista demotaan markovify-kirjastolla. Testaus ei ole vielä kattavaa, sillä suuri osa koodista on väliaikaista. PyQt5 tuottaa ongelmia 
pylintin kanssa, joten pylint-tulos on toistaiseksi huono. 

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

## Python-versio

Ohjelma on testattu python-versiolla 3.8.10, mutta kaikki python 3.8.0 korkeammat versiot pitäisi toimia.

## Dokumentaatio

- [Määrittelydokumentti](/Dokumentaatio/maarittelydokumentti.md/)
- [Työaikakirja](Dokumentaatio/tyoaikakirja.md/)

## Viikkoraportit

- [Viikko 1](/Dokumentaatio/viikkoraportti1.md/)
- [Viikko 2](/Dokumentaatio/viikkoraportti2.md/)
