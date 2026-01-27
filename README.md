# Prosjektbeskrivelse – IT-utviklingsprosjekt (2IMI)

##  Prosjekttittel

**Spillkveld (SPK)**

---

## Deltakere

Individuelt prosjekt

---

## 1. Prosjektidé og problemstilling

### Beskrivelse

Beskriv kort hva dere skal lage.

- Hva er prosjektet?

Ideén er å ha en nettside hvor folk kan snakke sammen om brettspill og søke de opp for å få info om de. Litt inspirasjon kommmer av nettsider som IMDB hvor du kan søke opp og legge igjen en anmeldelse. Uansett må sies at brettspill-siden legger mer vekt på å være sosialt medie. 

- Hvilket problem løser det?

Det er et samlet sted hvor man kan snakke om, anbefale og invitere til treff. Istedenfor å invitere på en meldingsgruppe og få en haug med meldinger tilbake, kan det funke mer som f.eks. Spond, en enkel oversikt over hvem som er og ikke er med.

- Hvorfor er løsningen nyttig?

Den gjør det klarere for deg og vennene dine hvem som skal bli med på et arrangement og man kan lese seg opp på spill før man møtes, så man ikke blir helt forvirret.

### Målgruppe

Hvem er løsningen laget for?

Løsningen er laget for de som spiller og liker brettspill, og de som er på spillekvelder.

---

## 2. Funksjonelle krav

Systemet skal minst ha følgende funksjoner:

1. Registrering

2. Innlogging

3. Søk

4. Invitér

5. Anmelde

---

## 3. Teknologivalg

### Programmeringsspråk
- Python, Javascript

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
- Navn:
- Beskrivelse:

**Tabell 2:**
- Navn:
- Beskrivelse:

*(Minst 2–4 tabeller)*

### Eksempel på tabellstruktur
```sql
User(
  id INT PRIMARY KEY,
  username VARCHAR(50),
  email VARCHAR(100),
  password VARCHAR(255)
)
