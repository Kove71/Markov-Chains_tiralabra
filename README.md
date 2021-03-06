# Markov-ketjut tekstin generoimisessa

Tiralabran projekti. Ohjelma generoi tekstiä korpustekstin perusteella käyttämällä markov-ketjua ja trie-datarakennetta.

## Nykyinen versio

Tekstin generointi on implementoitu vapaavalinteisella korpuksella ja markov-ketjun asteella. Tekstin generoimiseen käytetään trie-rakennetta.

## Asennus- ja käyttöohje

Ennen ensimmäistä käyttökertaa riippuvuudet tulee asentaa komennolla: 
```bash
poetry install
```
Ohjelma suoritetaan komennolla:
```bash
poetry run invoke start
```
Lint suoritetaan komennolla:
```bash
poetry run invoke lint
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

Ohjelma saattaa valittaa siitä, että nltk-kirjastoa ei ole asennettu. Jos tämä tapahtuu, suorita komento:
```bash
poetry run invoke dlnltk
```
Se asentaa 13mb-kokoisen tokenisaatiokirjaston. 

## Käyttöohje

Kun käynnistät ohjelman, voit testata valmiiksi ladattua korpusta kirjoittamalla 'greatgatsby.txt' tekstilaatikkoon. Parhaimmat tulokset tulee 3 tai 4 asteen ketjuilla. Markov Modelin luominen saattaa kestää hetken.

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
- [Viikko 6](/Dokumentaatio/viikkoraportti6.md/)
