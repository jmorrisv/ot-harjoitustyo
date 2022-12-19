# Käyttöohje

## Asennus

Mene projektin [etusivulle](https://github.com/jmorrisv/ot-harjoitustyo) ja lataa ohjelman uusin versio valitsemalla oikeasta yläkulmasta Code ja Download ZIP.

Asenna riippuvuudet komentoriviltä komennolla:

```poetry install```

Alusta ohjelma komennolla:

```poetry run invoke build```

Nyt voit käynnistää ohjelman komennolla:

```poetry run invoke start```

## Aloittaminen

Sovelluksen avautuessa näkyviin tulee tehtävälista. Jos käytät sovellusta ensimmäistä kertaa, lista on tyhjä. Pystyt lisäämään uuden siivottavan kohteen yksinkertaisesti painamalla Add new task -nappulaa.

![Tasks_new](https://user-images.githubusercontent.com/117164741/208421919-fd5fb194-1e34-4756-b15d-9c653079bc2f.JPG)

## Uuden tehtävän lisääminen

Add new task -napista painamalla pääset uuden tehtävän lisäysnäkymään.

![New_task_new](https://user-images.githubusercontent.com/117164741/208422537-83592eaa-e949-401b-8f8c-fd18f6147106.JPG)

Kirjoita tehtävälle kuvaava nimi name-kenttään. Frequency-kentissä voit määritellä tehtävälle toistuvuuden. Jos kirjoitat esimerkiksi

![Imuroi_new](https://user-images.githubusercontent.com/117164741/208422741-590b560d-9cac-428d-b7ef-866480cb6b29.JPG)

sovellus muistuttaa sinua imuroinnista viikon välein. Vinkkejä siihen, miten usein mikäkin kohde on hyvä siivota, löydät esimerkiksi [Marttaliiton](https://www.martat.fi/marttakoulu/kodinhoito/) sivuilta.

Huom. Mahdollisuus määritellä aika sekunteina on jätetty sovellukseen lähinnä sitä varten, ettei sovelluksen toimintaa testatakseen ole aina pakko odottaa päiviä, viikkoja tai kuukausia.

Tallenna tehtävä painamalla Save-nappia. Voit lisätä kerralla useita tehtäviä kirjoittamalla kenttiin uudet tekstit ja painamalla Save. Kun olet valmis, poistu näkymästä painamalla Close.

## Tehtävän merkitseminen siivotuksi

Tehtävälistalle lisätyt tehtävät näkyvät nyt aloitusnäkymässä. Kun kohde on aika siivota, se näkyy listassa ensimmäisenä, perässäään huutomerkki. Tartu imuriin, moppiin tai rättiin ja käy hommiin. Kun olet valmis, voit hyvällä omallatunnolla painaa Clean-nappulaa kohteen vieressä, jolloin huutomerkki poistuu.

![List_dirty_and_clean_new](https://user-images.githubusercontent.com/117164741/208423216-3c6eeab0-7587-431c-959f-79fabef8c045.JPG)

Voit siivota kohteen myös ennen, kuin huutomerkki ilmestyy. Tällöinkin Clean-nappulan painaminen asettaa kohteen ajastimen lähtemään alusta.

Huomaa, että sovellus ei päivity itsestään silloin, kun se on tehtävänäkymässä. Nähdäksesi ajantasaisen tiedon kohteiden likaisuudesta voit päivittää sovelluksen sulkemalla ja avaamalla sen uudestaan tai käymällä tehtävän lisäysnäkymässä ja palaamalla takaisin.

## Tehtävän tiedot

Tehtävän vieressä olevaa Info-nappia painamalla saat näkyviin info-ruudun, jossa näkyvät tehtävän tiedot: nimi, toistuvuus, seuraava siivouskerta ja siihen jäljellä oleva aika. Voit poistua näkymästä joko raksista tai Ok-napista.

![Imuroi_info_new](https://user-images.githubusercontent.com/117164741/208423714-dd218868-ea25-47d6-9f6c-2690e2afa214.JPG)

## Tehtävän poistaminen

Tehtävän vieressä olevasta Delete-napista painamalla tehtävä poistuu listasta ja tietokannasta pysyvästi.
