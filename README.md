# Prosjektbeskrivelse – IT-utviklingsprosjekt (2IMI)

## Prosjekttittel

**Internet Boardgame Database (IBDb)**

---

## Deltakere

Sivert M. H. (Individuelt prosjekt)

---

## 1. Prosjektidé og problemstilling

### Beskrivelse

- Hva er prosjektet?

Ideen er å lage en nettside for folk som er interreserte i brettspill. Brukeren skal kunne logge inn, registrere, søke og få info om brettspill, og mer. Litt inspirasjon kommmer av nettsider som imdb.com og boardgamegeek.com hvor du kan søke opp og legge igjen en anmeldelse, så jeg kan prøve å lage en slik funksjon.

- Hvilket problem løser det?

Nettsiden skal la deg som sagt søke opp brettspill og legge igjen anmeldelser. Dette kan man bruke som info til om man vil prøve et nytt et eller ikke, eller si noe om hvilke målgruppper spillet passer. Da slipper du å komme til spillekvelden med et spill ingen liker!

- Hvorfor er løsningen nyttig?

Nettsiden funker som et oppslagsverk for brettspill. Det betyr at du kan søke opp spill du allerede har for å se hva andre enn deg synes om det. Dersom du ikke har et spill kan du bruke nettsiden til å finne et nytt et som er gøy.

### Målgruppe

Hvem er løsningen laget for?

Løsningen er laget for de som spiller og liker brettspill, og de som vil finne ut mer om de. Det kan f.eks. være før de velger å kjøpe det, eller ikke pga dårlige anmeldelser.

### Refleksjon



---

## 2. Funksjonelle krav

Systemet skal minst ha følgende funksjoner:

1. Registrering

2. Innlogging

3. Søke etter brettspill

4. Registrere brettspill (hvis du er admin)

5. Anmelde

---

## 3. Teknologivalg

### Programmeringsspråk

- Python

### Rammeverk / Plattform / Spillmotor

- Flask

### Database

- MariaDB

### Verktøy

- GitHub
- GitHub Projects (Kanban)
- Figma

---

## 4. Datamodell

### Oversikt over tabeller

**Tabell 1:**

- Navn: user
- Beskrivelse: Innholder brukerinfo om email, brukernavn og et hashet og saltet passord.

**Tabell 2:**

- Navn: boardgame
- Beskrivelse: Inneholder navnet (til brettspillet), hvilket år det kom ut, de som lagde det, de som publiserte det og en beskrivelse. 

_(Minst 2–4 tabeller)_

### Eksempel på tabellstruktur

```sql
`user` (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255) NOT NULL UNIQUE,
email VARCHAR(255) NOT NULL UNIQUE,
password CHAR(60) NOT NULL,
role VARCHAR(50)
)
```

**Kilder:**

dotenv: [https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/](https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/)

bcrypt hashing: [https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/](https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/)

bytte brukernavn Mysql: [https://dev.mysql.com/doc/refman/8.4/en/rename-user.html](https://dev.mysql.com/doc/refman/8.4/en/rename-user.html)

få liste av alle brukere i Mysql: [https://phoenixnap.com/kb/mysql-show-users](https://phoenixnap.com/kb/mysql-show-users)

Bytte passord i Mysql: [https://dev.mysql.com/doc/refman/8.4/en/alter-user.html](https://dev.mysql.com/doc/refman/8.4/en/alter-user.html)

Bcrypt CHAR(60): [https://stackoverflow.com/questions/5881169/what-column-type-length-should-i-use-for-storing-a-bcrypt-hashed-password-in-a-d](https://stackoverflow.com/questions/5881169/what-column-type-length-should-i-use-for-storing-a-bcrypt-hashed-password-in-a-d)

Datatyper i SQL: [https://www.geeksforgeeks.org/sql/sql-data-types/](https://www.geeksforgeeks.org/sql/sql-data-types/)

Innholdstekst osv av Boardgamegeek: [https://boardgamegeek.com](https://boardgamegeek.com)

Flash med flask: [https://flask.palletsprojects.com/en/stable/patterns/flashing/](https://flask.palletsprojects.com/en/stable/patterns/flashing/)