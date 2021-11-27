# Toteutusdokumentti

## Tietorakenne

### Toteutus

Sovellus käyttää tietorakenteena trie-tietorakennetta. Sen toiminallisuus on jaettu kahteen luokkaan: TrieNode ja Trie. 
Ensiksi Trie hakee tokenisoidun tekstin ja alustaa TrieNode-olion, joka on trierakenteen juuri, ja trien "syvyyden", eli kuinka monta
sanaa esiintyy tallenettavassa sanamonikossa. Tokenisoitu teksti on tallenettu sisäkkäisenä listana, jossa jokainen sisäkkäinen lista on oma lauseensa. 

TrieNode on trie-rakenteen sana/solmu. Sen attribuutteja ovat sana, syvyys, esiintymismäärä ja sen lapset.

Trie luo edellämainittujen asioiden avulla puun käyttäen create_tree()-metodia. Trie käy tokenisoidun tekstin läpi lauseittain. Se käy lauseen jokaisen sanan läpi, ja kutsuu metodia add_ngram(), jolle annetaan parametriksi lisättävä monikko. add_ngram() asettaa ensiksi juuren solmuksi. Seuraavaksi se 
käy monikon jokaisen sanan läpi. Ensiksi tarkistetaan, onko käsiteltävä sana nykyisen solmun (joka on aluksi juuri) lapsi. Jos ei, sana lisätään solmun lapseksi
luomalla uusi TrieNode-olio ja nykyinen solmu vaihtuu juuri lisättyyn solmuun. Jos sana löytyy nykyisen solmun lapsista, vaihdetaan nykyinen solmu löydettyyn solmuun ja lisätään sen esiintymismäärää yhdellä.

Trie-luokalla on myös find_ngram()-metodi. Se saa parametrikseen monikon, joka pitää löytää trie-rakenteesta. Solmuksi asetetaan trien juuri, jonka jälkeen metodi käy monikon sanat läpi kerrallaan. Jos sana löytyy nykyisen solmun lapsista, vaihdetaan solmu lapseen, ja sen lapset asetetaan children-listaan. Jos sanaa ei löydy, palautetaan None. Kun kaikki monikon lapset on löydetty, palautetaan children-lista.

### Aikavaativuus

Ideaalisti trien luominen tapahtuu ajassa O(nm), jossa n on sanojen määrä ja m on sanojen määrä monikossa ("syvyys"). Toistaiseksi trien rakentaminen kestää huomattavasti hitaammin, sillä TrieNoden lapset tallenetaan listaan, jolloin lista pitää käydä läpi useasti. Vaihdan sen ensi viikolla pythonin dictionaryyn, jolloin rakentaminen on huomattavasti nopeampaa. Sanan etsiminen tapahtuu ideaalisti ajassa O(n), jossa n on monikon sanojen määrä.

## Markov-Ketju

### Toteutus

Sovellus käyttää markov-ketjua tekstin generointiin. Sen toiminallisuus tapahtuu luokassa MarkovChain. 

MarkovChain-luokka alustaa ensiksi Trie-luokan, joka saa parametreikseen markov-ketjuun asteen + 1, joka on trien syvyys, ja tokenisoidun tekstin, joka saadaan käyttämällä tokenize()-metodia. 

MarkovChain-luokan generate_text()-metodi on vastuussa tekstin luomisesta. Se alustaa generated_text-muuttujan, joka on tyhjä string. Seuraavaksi se hakee lauseen ensimmäisen sanan ja antaa sen parametriksi add_sentence()-metodille. add_sentence()-metodi alustaa ensiksi prior_state-listan, jossa on lista lisätyistä sanoista. Sen maksimipituus on ketjun aste.

### Aikavaativuus

Tekstin generointi tapahtuu aikavaativuudessa O(nmo), jossa n on ketjun aste, m on lauseen pituus ja o lauseiden määrä.