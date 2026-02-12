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

Ideen er å lage en nettside for folk som er interreserte i brettspill. Brukeren skal kunne logge inn, registrere, søke og få info om brettspill, og om du er admin/editor, kunne legge til brettspill i databasen. Litt inspirasjon kommmer av nettsider som IMDb og Boardgamegeek.

- Hvilket problem løser det?

Nettsiden skal la deg som sagt søke opp brettspill og finne info om de. Dette kan man bruke som et verktøy for å researche spillet eller si noe om hvilke målgruppper spillet passer. Da slipper du å komme til spillekvelden med et spill ingen liker!

- Hvorfor er løsningen nyttig?

Nettsiden funker som et oppslagsverk for brettspill. Det betyr at du kan søke opp spill du allerede har for kanskje å hvordan det spilles om du f.eks. mistet reglene. Dersom du ikke har et spill kan du bruke nettsiden til å lese deg opp på nett isteden for å måtte dra til byen eller kjøpesenteret.

### Målgruppe

Hvem er løsningen laget for?

Løsningen er laget for de som spiller og liker brettspill, og de som vil finne ut mer om de. Det kan f.eks. være før de velger å kjøpe det, eller ikke, p.g.a. det de leste om det. Det kan også f.eks. være de som har mistet regler og glemte hva målet i spillet var som bruker siden for å minne seg selv på dette.

### Refleksjon

#### Resultat

Dette er jo det andre ordentlige Flask-prosjektet vi har hatt med 2IMI, og denne gangen gikk det bedre. En god grunn til dette er at målet var mer realistisk å oppnå denne gangen. Det var mye mer produktivt å ha en gjennomførbar plan. Da går motivasjonen opp og man blir ikke sittende stille å tenke på hvor man skal begynne, isteden fører det til en effekt av en positiv "snowball"-effekt. 

På den andre siden gikk noen ting kanskje ikke akkurat etter plan. For eksempel så fokuserte jeg lite på nettsidens stylesheet, litt som sist, selv om jeg ville bruke lenger tid på dette. En ting til var at jeg undergravde viktigheten av innhold i databasen. Mer tid burde blitt satt av bare til å legge til nye brettspill, slik at funksjonene blir ordentlig vist frem.

Uansett vil jeg vi at dette prosjektet på mange måter var en forbedring fra forrige gang. Noen feil ble repetert, i tillegg til at nye oppsto. Totalt sett fra dette prosjektet har lært enormt mye nytt, fra å lage innloggings-side med Session, lagre passord trygt i en database med Bcrypt, og helt til å lage søke-funksjon i Python/Flask.

#### Mulige Forbedringer

Det er noen funksjoner og aspekter til prosjektet som kunne trengt forbedring. Enten om det er en revisjon av noe eller en helt ny funksjon. Her er noen konkrete ideer basert på min brukertesting:

**Ville brukt litt mer tid på stil**

Selv om dette ikke er hovedfokuset med et slikt prosjekt, blir det enklere å brukerteste med en nettside som ser ordentlig ut. Også, om man presenterer prosjektet til noen andre vil det være enklere å forstå hva nettsiden gjør om man har et bedre visuelt layout.

**Egen side for hvert spill**

Dette kan nesten klassifiseres som en manglende funksjon. Hver av spillene på forsiden, eller hvis du søker de opp, burde ha sin egen side hvor du får flere detaljer og beskrivelse av spillet. Selv om dette ikke sto i målene jeg satt, er ikke nettsiden helt komplett uten. Hvis jeg velger å fortsette på prosjektet, er dette en viktig del.

**Brukeradministrering**

Admin har oversikt over brukere og kan angi roller. Man slipper da å manuelt gå inn i database med SSH. Dette gir også en reell grunn til å ha en editor-rolle, da admin har samme tillatelser som editor, og nå faktisk fler.

**Rolleindikator**

Muligheten til å se hva slags rolle din bruker har. Det kan gjøres ved å ha tekst i navbar eller i navbar men i dropdown når man er logget inn.

**Innloggingsstatus**

Dette ligner en del på rolleindikator-ideen, men enklere. Brukeren kan se at de er logget inn. Kan gjøres ved å vise brukernavn i navbar.

---

## 2. Funksjonelle krav

Systemet skal minst ha følgende funksjoner:

1. Registrering

2. Innlogging

3. Søke etter brettspill

4. Registrere brettspill (om admin/editor)

5. Ulikt innhold/tillatelser basert på rolle (registrering av brettspill)

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

---

## 4. Datamodell

### Oversikt over tabeller

**Tabell 1:**

- Navn: user
- Beskrivelse: Innholder brukerinfo om email, brukernavn og et hashet og saltet passord.

**Tabell 2:**

- Navn: boardgame
- Beskrivelse: Inneholder navnet (til brettspillet), hvilket år det kom ut, de som lagde det, de som publiserte det og en beskrivelse.

**Tabell 3:**

- Navn: role
- Beskrivelse: Inneholder forskjellige roller som brukere kan ha. Her må jeg kjøre en manuell Insert, eller lage en funksjon i Python-filen.

### Tabellstruktur i Databasen

```sql
-- Tabell 1

CREATE TABLE `user` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password CHAR(60) NOT NULL,
    role_id INT, FOREIGN KEY (role_id) REFERANCES role(id)
);

-- Tabell 2

CREATE TABLE boardgame (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year_published INT,
    creator VARCHAR(255),
    publisher VARCHAR(255),
    description TEXT CHARACTER SET utf8mb4
    );

-- Tabell 3

CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20)
)

-- Innhold til tabell 3

INSERT INTO role (name) VALUES ("admin"), ("editor"), ("user");

-- Rolle-tabellens innhold ser dermed slik ut:

+----+--------+
| id | name   |
+----+--------+
|  1 | admin  |
|  2 | editor |
|  3 | user   |
+----+--------+
-- Her ser man hvilke id som tilhører hvilke rolle
```

---

**Kilder:**

dotenv: [https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/](https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/)

bcrypt hashing: [https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/](https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/)

bytte brukernavn Mysql: [https://dev.mysql.com/doc/refman/8.4/en/rename-user.html](https://dev.mysql.com/doc/refman/8.4/en/rename-user.html)

få liste av alle brukere i Mysql: [https://phoenixnap.com/kb/mysql-show-users](https://phoenixnap.com/kb/mysql-show-users)

Bytte passord i Mysql: [https://dev.mysql.com/doc/refman/8.4/en/alter-user.html](https://dev.mysql.com/doc/refman/8.4/en/alter-user.html)

Bcrypt CHAR(60): [https://stackoverflow.com/questions/5881169/what-column-type-length-should-i-use-for-storing-a-bcrypt-hashed-password-in-a-d](https://stackoverflow.com/questions/5881169/what-column-type-length-should-i-use-for-storing-a-bcrypt-hashed-password-in-a-d)

_SQL Data Types_: [https://www.geeksforgeeks.org/sql/sql-data-types/](https://www.geeksforgeeks.org/sql/sql-data-types/)

Innholdstekst tatt fra Boardgamegeeks nettsider: [https://boardgamegeek.com](https://boardgamegeek.com)

Flash med flask: [https://flask.palletsprojects.com/en/stable/patterns/flashing/](https://flask.palletsprojects.com/en/stable/patterns/flashing/)

Lage roller i mysql (system, ikke i oppgave): [https://www.geeksforgeeks.org/sql/sql-creating-roles/](https://www.geeksforgeeks.org/sql/sql-creating-roles/)

_How to use Flask-Session in Python Flask_: [https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/](https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/)

_Building a Search Feature in a Python Flask App_: [https://ochoaprojects.com/posts/FlaskAppWithSimpleSearch/](https://ochoaprojects.com/posts/FlaskAppWithSimpleSearch/)

_MySQL LIKE Operator_:[https://www.w3schools.com/mysql/mysql_like.asp](https://www.w3schools.com/mysql/mysql_like.asp)
