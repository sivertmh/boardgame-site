# Prosjektbeskrivelse – IT-utviklingsprosjekt (2IMI)

##  Prosjekttittel

**Internet Boardgame Database (IBDb)**

---

## Deltakere

Sivert M. H. (Individuelt prosjekt)

---

## 1. Prosjektidé og problemstilling

### Beskrivelse

Beskriv kort hva dere skal lage.

- Hva er prosjektet?

Ideén er å ha en nettside hvor folk kan snakke sammen om brettspill, anmelde de og søke de opp for å få info om de. Litt inspirasjon kommmer av nettsider som IMDB hvor du kan søke opp og legge igjen en anmeldelse. Uansett må sies at brettspill-siden legger mer vekt på å være sosialt medie. 

- Hvilket problem løser det?

Det er et samlet sted hvor man kan snakke om, anbefale og invitere til treff. Istedenfor å invitere på en meldingsgruppe og få en haug med meldinger tilbake, kan det funke mer som f.eks. Spond, en enkel oversikt over hvem som er og ikke er med.

- Hvorfor er løsningen nyttig?

Den gjør det klarere for deg og vennene dine hvem som skal bli med på et arrangement og man kan lese seg opp på spill før man møtes, så man ikke blir helt forvirret.

### Målgruppe

Hvem er løsningen laget for?

Løsningen er laget for de som spiller og liker brettspill, og de som vil finne ut mer om de. Det kan være før de velger å kjøpe det f.eks..

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
- Navn:
- Beskrivelse:

*(Minst 2–4 tabeller)*

### Eksempel på tabellstruktur

```sql
User(
  id INT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password CHAR(60) NOT NULL
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