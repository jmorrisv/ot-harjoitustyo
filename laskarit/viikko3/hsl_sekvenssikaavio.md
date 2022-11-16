```mermaid
sequenceDiagram
main ->> laitehallinto: HKLLaitehallinto()
main ->> rautatietori: Lataajalaite()
main ->> ratikka6: Lukijalaite()
main ->> bussi244: Lukijalaite()
main ->> laitehallinto: lisaa_lataaja(rautatietori)
main ->> laitehallinto: lisaa_lukija(ratikka6)
main ->> laitehallinto: lisaa_lukija(bussi244)
main ->> lippu_luukku: Kioski()
main ->> lippu_luukku: osta_matkakortti("Kalle")
activate lippu_luukku
lippu_luukku ->> kallen_kortti: Matkakortti("Kalle")
lippu_luukku -->> main: 
deactivate lippu_luukku
