# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjää pitämään kirjaa kodin siivoustöistä. Sovellukseen voi tallentaa siivottavia kohteita ja määritellä niille siivousvälin. Sovellus ilmoittaa, kun kukin kohde on aika siivota. Inspiroiduin puhelimessani olevasta Sweepy-siivoussovelluksesta, josta toteutan yksinkertaisen version.

## Käyttöliittymäluonnos

Sovellus koostuu kahdesta näkymästä.
![IMG_20221114_100911](https://user-images.githubusercontent.com/117164741/201608205-4fc469fb-bb5b-4cd3-afc0-4eaabd7ac2bc.jpg)
Sovellus avautuu listanäkymään, joka on tyhjä ennen kuin listaan on lisätty jotain. NEW-napista avautuu näkymä, jossa voi lisätä uudelle kohteelle nimen ja toistuvuuden. Jos käyttäjä tallentaa kohteen, se ilmestyy listalle. Kun aika on kulunut umpeen, kohteen perään ilmestyy !-merkki. Se poistuu CLEAN-napista painamalla. CLEAN-nappia voi painaa minkä tahansa kohteen kohdalla koska vain, jolloin kohteen ajastin alkaa alusta.

## Perusversion toiminnallisuus

### Yleisnäkymässä
- Käyttäjä näkee kaikki tallennetut kohteet.
- Kohteet, joiden ajastin on kulunut loppuun, ovat likaisia. Niiden kohdalla on merkintä !
- Käyttäjä voi merkitä minkä tahansa kohteen siivotuksi, jolloin sen ajastin lähtee käyntiin alusta.

### New Task -näkymässä
- Käyttäjä määrittelee uudelle kohteelle nimen ja toistuvuuden.
- Kohteen voi tallentaa tai poistua näkymästä tallentamatta.

## Jatkokehitysideoita
- Sovellus näyttää kunkin kohteen kohdalla ajan seuraavaan siivouskertaan.
- Kohteen voi poistaa.
- Kohteita voi ryhmitellä esim. huoneen mukaan.
