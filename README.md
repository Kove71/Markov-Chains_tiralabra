# Markov-ketjut tekstin generoimisessa

Tiralabran projekti. Ohjelma generoi tekstiä korpustekstin perusteella käyttämällä markov-ketjua ja trie-datarakennetta.

## Nykyinen versio

Tekstin generointi on implementoitu vapaavalinteisella korpuksella ja markov-ketjun asteella. Tekstin generoimiseen käytetään trie-rakennetta. Testaus ei ole vielä kattavaa.

## Asennusohje

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

Ohjelma saattaa valittaa siitä, että nltk-kirjastoa ei ole asennettu. Jos tämä tapahtuu, suorita komento:
```bash
poetry run python3 src/dlnltk.py
```
Se asentaa 13mb-kokoisen tokenisaatiokirjaston. 

## Käyttöohje

Kun käynnistät ohjelman, voit testata valmiiksi ladattua korpusta kirjoittamalla 'greatgatsby.txt' tekstilaatikkoon. Parhaimmat tulokset tulee 4 tai 5 asteen ketjuilla. Markov Modelin luominen saattaa kestää hetken.

## Python-versio

Ohjelma on testattu python-versiolla 3.8.10, mutta kaikki python 3.8.0 korkeammat versiot pitäisi toimia.

## Dokumentaatio

- [Määrittelydokumentti](/Dokumentaatio/maarittelydokumentti.md/)
- [Työaikakirja](Dokumentaatio/tyoaikakirja.md/)
- [Testausdokumentti](Dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](Dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit

- [Viikko 1](/Dokumentaatio/viikkoraportti1.md/)
- [Viikko 2](/Dokumentaatio/viikkoraportti2.md/)
- [Viikko 3](/Dokumentaatio/viikkoraportti3.md/)
- [Viikko 4](/Dokumentaatio/viikkoraportti4.md/)
- [Viikko 5](/Dokumentaatio/viikkoraportti5.md/)

