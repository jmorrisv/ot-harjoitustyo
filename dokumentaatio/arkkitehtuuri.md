# Arkkitehtuurikuvaus

## Rakenne

Sovellus tulee koostumaan neljästä hakemistosta. Ui tulee vastaamaan käyttöliittymästä. Se on erotettu sovelluslogiikasta. En ole vielä toteuttanut sitä. Services vastaa ohjelman toiminnallisuuksista ja
sovelluslogiikasta. Se toimii tavallaan käyttöliittymän ja sovelluksen muiden osien välissä. Entities- hakemistossa on kaksi luokkaa, siivottavia kohteita kuvaava Task
sekä ajastin eli Timer. Repositories-hakemisto vastaa tietojen tallentamisesta ja tallennettujen tietojen hakemisesta tietokannasta.

## Sovelluslogiikka

Sovellus käsittelee tehtäviä Task-luokan mukaisina olioina. Task-luokka käyttää Timer-ajastinta puhtauden tai likaisuuden määrittelyyn.

Services-luokassa on suurin osa ohjelman toiminnallisuudesta. Sieltä löytyy esim. seuraavat metodit:
- get_all_tasks() 
- add_new_task()
- mark_done()

Repositories tallentaa tehtäviä tietokantaan ja palauttaa sovelluksen käyttöön listoja tallennetuista tehtävistä.

Alla oleva pakkauskaavio havainnollistaa visuaalisesti luokkien suhteita.

![download](https://user-images.githubusercontent.com/117164741/205582043-65f0893c-3fbd-4b74-8052-98ddc0d4c3ff.png)

## Toiminnallisuus

### Uuden tehtävän lisääminen

Käyttäjä lisää uuden tehtävän ja syöttää sen tiedot, eli nimen ja toistuvuuden.

```mermaid
sequenceDiagram
participant User
participant Ui
participant Services
participant TaskRepository
participant Timer
User ->> Ui: Click Add New Task button
activate Ui
Ui ->> Services: create_new_task(name, seconds)
Services ->> TaskRepository: TaskRepository()
activate Services
Services ->> Task: Task(name, frequency=timedelta(seconds=seconds))
activate Task
Task ->> Timer: Timer(frequency)
Task -->> Services: task
deactivate Task
Services ->> TaskRepository: add_new_task(task)
activate TaskRepository
TaskRepository ->> Timer: set()
activate Timer
Timer -->> TaskRepository: end_time
deactivate Timer
TaskRepository ->> Database: write_new_task(task, frequency, end_time)
TaskRepository -->> Services: 
deactivate TaskRepository
Services -->> Ui: 
deactivate Services
deactivate Ui
```

Käyttöliittymä antaa Services-luokalle tehtävän. Services kutsuu Task-luokkaa muodostaakseen tiedoista olion, ja välittää tämän olion TaskRepository-luokalle, joka
tallentaa sen tietokantaan.
