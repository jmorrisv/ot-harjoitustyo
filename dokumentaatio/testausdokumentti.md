# Testausdokumentti

Ohjelman toimivuutta on testattu automaattisilla Unittest-testeillä. Käyttöliittymä on jätetty unittest-testien ulkopuolelle ja sitä on testattu manuaalisesti erilaisilla skenaarioilla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluksen toiminnallisuutta testaa luokka TestServices. Luokka testaa tehtävän lisäämiseen ja tehtävälistan näyttämiseen liittyvät metodit ja virheilmoitukset erilaisilla tilanteilla. Luokka alustaa uuden tietokannan ja luo siihen testitehtäviä. Ajastin on testattu vielä erikseen TestTimer-luokan avulla.

### Repositoriot

TestTaskRepository-luokka testaa repositorion tärkeimmät metodit.

### Testikattavuus

Testikattavuus on 78%. Tärkeimmät kattavuuden ulkopuolelle jääneet asiat ovat uusimmat metodit, eli tehtävän tietojen näyttäminen sekä tehtävän poistaminen. Näitä on kuitenkin testattu manuaalisesti monella erilaisella skenaariolla.

![Testikattavuus221219](https://user-images.githubusercontent.com/117164741/208426748-613f3644-3c47-455a-a6c4-320c6c852c67.JPG)

## Järjestelmätestaus

Järjestelmätestaus on toteutettu manuaalisesti.

## Asennus ja konfigurointi

Ohjelman lataaminen on testattu useassa eri Linux-ympäristössä.
Ohjelma on testattu avata sekä sellaisessa tilantessa, jossa valmista tietokantatiedostoa ei ole, että silloin, kun sellainen on.

## Toiminnallisuus

Määrittelydokumentissa ja käyttöohjeessa mainitut toiminnallisuudet on toteutettu ja testattu toimiviksi erilaisilla syötteillä. Virheellisiä syötteitä on testattu sekä manuaalisesti, että automaattisesti.

## Laatuongelmat

- Sovellusta on testattu ainoastaan lyhyellä aikavälillä. Ei ole testattu, toimivatko sovelluksen ajastinominaisuudet oikein esim. usean kuukauden aikavälillä.
- Sovelluken konfiguraatiossa on puutteita. Sovellus ei käytä erillisessä tiedostossa määriteltyjä ympäristömuuttujia, jolloin testeille voisi määritellä omat testimuuttujat. Tästä syystä testien suorittaminen pyyhkii pois kaikki aiemmat tallennukset.
