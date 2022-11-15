```mermaid
 classDiagram
      Monopoli "1" -- "1" Pelilauta
      Monopoli "1" -- "2..8" Pelaaja
      Pelilauta "1" -- "40" Ruutu
      Ruutu : seuraava
      Pelaaja "1" -- "1" Nappula
      Ruutu "1" -- "0..8" Nappula
      Monopoli "1" -- "2" Noppa
      Pelaaja ..> Noppa
```
