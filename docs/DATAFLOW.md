# Data Flow

## Overordnet System Flow

### 1. Data Indsamling

#### Chatbot Data
- Data modtages via webhook fra eksisterende chatbot system
- Webhook payload gemmes direkte i databasen
- Konverteres til vector format for senere analyse

#### Email Data
- Emails forwardes til dedikeret email adresse
- System monitorer og processerer indkomne emails
- Gemmes i databasen og konverteres til vector format
- Emails grupperes i tråde baseret på subject og references

#### Hjemmeside Data
- Data indsamles fra kundens hjemmeside
- Konverteres til vector format
- Gemmes i databasen med relation til CVR

#### Dokumenter
- Uploades manuelt til systemet
- Kategoriseres efter type
- Konverteres til vector format for analyse

### 2. Data Processering

#### Lead Håndtering i CRM
1. Bruger vælger/klikker på et lead i CRM systemet
2. System identificerer al relevant data via CVR:
   - Chatbot historik
   - Email korrespondance
   - Uploadede dokumenter
   - Hjemmeside data

#### Analyse Process
1. System analyserer den samlede data:
   - Gennemgår chatbot interaktioner
   - Analyserer email korrespondance
   - Inddrager relevante dokumenter
   - Inkluderer hjemmeside data

#### Output Generering
1. Genererer anbefalinger til næste skridt
2. Udfører prisberegning baseret på tilgængelig data

### 3. Data Lagring

Al data gemmes struktureret i Supabase:
- Rå data bevares i original form
- Vector embeddings for effektiv søgning
- Relationer via CVR-nummer
- Metadata og timestamps for spørbarhed

## Systemintegration

### Input Endpoints
1. Chatbot Webhook Endpoint
   - Modtager data fra chatbot system
   - Validerer payload
   - Initierer dataprocessering

2. Email Modtagelse
   - Dedikeret email adresse
   - Email parsing og processering
   - Tråd-identificering

### Output Generering
1. Anbefalings Engine
   - Analyserer kombineret data
   - Genererer prioriterede forslag
   - Baserer forslag på historisk data

2. Prisberegnings Engine
   - Inddrager relevante prisdata
   - Beregner baseret på definerede regler
   - Gemmer delresultater for transparens

## Fejlhåndtering

### Data Modtagelse
- Validering af indkomne data
- Fejllog ved ukorrekt data
- Automatisk notifikation ved kritiske fejl

### Processering
- Backup af rå data
- Fejltolerant vector konvertering
- Transaktionel datahåndtering

## Monitorering

### System Health
- Overvågning af datainput
- Kontrol af processeringstider
- Kvalitetskontrol af anbefalinger

### Performance Metrics
- Svartider på analyser
- Præcision af anbefalinger
- Systembelastning ved dataprocessering