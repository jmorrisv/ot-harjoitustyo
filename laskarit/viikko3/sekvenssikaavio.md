```mermaid
sequenceDiagram
Main ->> car: Machine()
car ->> tank: FuelTank()
car ->>+ FuelTank: car._tank.fill(40)
FuelTank ->> tank: 40
FuelTank -->>- car: 
