# Siivousapuri

Sovellus auttaa käyttäjäänsä pitämään kotinsa siistinä. Sovelluksen listaan voi tallentaa siivottavia kohteita ja asettaa niille toistuvuuden. Sovellus pitää kirjaa kohteista ja ilmoittaa kunkin kohteen kohdalla, kun se on aika siivota.

## Dokumentaatio

- [Käyttöohje](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

- [Tuntikirjanpito](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

- [Testausdokumentti](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)

- [Viikon 5 release](https://github.com/jmorrisv/ot-harjoitustyo/releases/tag/viikko5)

- [Viikon 6 release](https://github.com/jmorrisv/ot-harjoitustyo/releases/tag/viikko6)

- [Loppupalautus](https://github.com/jmorrisv/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus

Asenna riippuvuudet komennolla:

```
poetry install
```

Alusta ohjelma komennolla:

```
poetry run invoke build
```

Nyt voit käynnistää ohjelman komennolla:

```
poetry run invoke start
```

## Komentorivikomennot

Ohjelma käynnistyy komennolla:

```
poetry run invoke start
```

Voit suorittaa testit komennolla:

```
poetry run invoke test
```

Saat testikattavuusraportin komennolla:

```
poetry run invoke coverage-report
```

Löydät tämän jälkeen raportin syntyneestä htmlcov-hakemistosta.

Pylint-tarkistukset voi tehdä komennolla:

```
poetry run invoke lint
```

Pylint suorittaa tarkistuksen [tämän](https://github.com/jmorrisv/ot-harjoitustyo/blob/main/.pylintrc) tiedoston mukaisesti.
