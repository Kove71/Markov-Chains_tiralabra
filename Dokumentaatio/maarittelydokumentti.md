# Määrittelydokumentti

## Aihe ja toteutus

Valitsin projektin aiheeksi tekstin generoimisen markov-ketjujen avulla. Siinä tekstidatasta luodaan probabilistinen malli, jossa sanoilla on erilaiset 
todennäköisyydet erilaisille tilasiirtymillle toisiin sanoihin. Aihe kiinnosti minua siksi, koska teen sivuaineenani kieliteknologiaa. Kuvittelsin, että 
yksinkertaisestakin tekstintuotto-ohjelmasta on paljon hyötyä kieliteknologian ymmärtämisessä.

## Projektin kieli
Ohjelma toteutaan pythonilla. Javan taitoni ovat aika heikot, minkä takia en usko, että voin antaa hyvää vertaispalautetta Java-projekteille.

## Projektissa käytettävät algoritmit ja tietorakenteet

### Tietorakenteet
Tietorakenteena käytetään trie-tietorakennetta. Siinä luodaan puu, jossa solmut ovat sanojen merkit.

### Algoritmit

Projekti käyttää markov-ketjuja luodakseen stokastisen mallin tekstistä. Mallin perusteella algoritmi 
pystyy muodostamaan uusia sanoja edellisten sanojen perusteella.

## Tavoitteena olevat aika- ja tilavaativuudet

- Trie-datarakenne
  - Aikavaativuus sanan etsimisessä ja lisäämisessä on O(n), jossa n on sanan merkkien määrä.
  - Tilavaativuus on O(n), jossa n on kaikkien sanojen merkkien määrä.


## Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti, Helsingin yliopisto. 

## Lähteet

- https://www.kdnuggets.com/2019/11/markov-chains-train-text-generation.html
- https://en.wikipedia.org/wiki/Trie
- https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e#4316



