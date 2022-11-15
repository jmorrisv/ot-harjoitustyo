```mermaid
 classDiagram
      Pelilauta "1" -- "40" Ruutu
      Pelaaja "1" -- "1" Nappula
      Ruutu "1" -- "0..8" Nappula
      Pelilauta "1" -- "2..8" Nappula
      class Noppa
```
