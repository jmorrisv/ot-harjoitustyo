# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa käyttäjää pitämään kirjaa kodin siivoustöistä. Sovellukseen voi tallentaa siivottavia kohteita ja määritellä niille siivousvälin. Sovellus ilmoittaa, kun kukin kohde on aika siivota. Inspiroiduin puhelimessani olevasta Sweepy-siivoussovelluksesta, josta toteutan yksinkertaisen version.

## Käyttöliittymäluonnos

Sovellus koostuu kahdesta näkymästä.
![IMG_20221114_100911](https://user-images.githubusercontent.com/117164741/201608205-4fc469fb-bb5b-4cd3-afc0-4eaabd7ac2bc.jpg)
Sovellus avautuu listanäkymään, joka on tyhjä ennen kuin listaan on lisätty jotain. ADD NEW TASK-napista avautuu näkymä, jossa voi lisätä uudelle kohteelle nimen ja toistuvuuden. Jos käyttäjä tallentaa kohteen, se ilmestyy listalle. Tehtävän lisäys -näkymästä voi poistua myös tallentamatta. Toisin kuin luonnoksessa, valmiissa sovelluksessa aika määritellään kuukausina, viikkoina, päivinä ja sekunteina. Tämä siksi, että yleensä kodin kohteita ei siivota tuntien tai minuuttien välein. Sekunnit ovat valmiissa sovelluksessa, jotta käytön testaaminen on helpompaa.

Kun aika on kulunut umpeen, kohteen perään ilmestyy !-merkki. Se poistuu CLEAN-napista painamalla. CLEAN-nappia voi painaa minkä tahansa kohteen kohdalla koska vain, jolloin kohteen ajastin alkaa alusta.

Listanäkymään tulee jokaisen kohteen kohdalle myös DELETE-nappula, josta kohteen voi poistaa, sekä INFO-nappula. INFO-nappulaa painamalla ilmestyy näkyviin ponnahdusikkuna, jossa on kohteen tiedot: nimi, toistuvuus, seuraava siivousaika ja siihen jäljellä oleva aika.

## Perusversion toiminnallisuus

### Tehtävälistanäkymässä
- Käyttäjä näkee kaikki tallennetut kohteet.
- Kohteet, joiden ajastin on kulunut loppuun, ovat likaisia. Niiden kohdalla on merkintä !
- Likaiset kohteet näkyvät listalla ensin.
- Käyttäjä voi merkitä minkä tahansa kohteen siivotuksi, jolloin sen ajastin lähtee käyntiin alusta.
- Kohteen voi poistaa.
- Käyttäjä näkee nappia painamalla kohteen tiedot, kuten toistuvuuden ja ajan seuraavaan siivouskertaan.

### Add new task -näkymässä
- Käyttäjä määrittelee uudelle kohteelle nimen ja toistuvuuden.
- Kohteen voi tallentaa tai poistua näkymästä tallentamatta.
- Useita kohteita voi tallentaa perätysten ennen paluuta listanäkymään.

## Jatkokehitysideoita
- Sovellus päivittää tehtävälistaa jatkuvasti ollessaan listanäkymässä.
- Kohteita voi ryhmitellä esim. huoneen mukaan.
- Kohteita voi muokata tallentamisen jälkeen.
- Sovelluksella voi olla useita käyttäjiä.
- Käyttäjät voivat kilpailla siitä, kuka siivoaa eniten.
