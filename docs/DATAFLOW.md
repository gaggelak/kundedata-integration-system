# Data Flow

## System Overblik

Systemet består af følgende hovedkomponenter:

1. **CRM Platform (Frontend)**
   - Tilgængelig på `https://jeres-crm.dk`
   - Brugerlogin med credentials
   - Adgang til data baseret på CVR-nummer
   - Præsentation af al data og analyse

2. **Backend API**
   - Hostet på DigitalOcean
   - Håndterer alle datastrømme
   - Udfører analyse og beregninger
   - Leverer data til frontend

3. **Database (Supabase)**
   - Cloud-hosted database
   - Gemmer al struktureret data
   - Vector storage for tekstanalyse
   - Brugerautentificering

## Data Flow Diagram
```
[Chatbot] ───webhook───→ [Backend API] ───→ [Supabase]
[Emails]  ───email───→      ↑               ↑
[Upload]  ───files───→      |               |
                             |               |
[CRM Interface] ←───────API calls──────────∝
```

## Data Strømme

### 1. Indgående Data

#### Chatbot Data
- Wotnot sender samtaler via webhook
- Data inkluderer samtalehistorik og metadata
- Tilknyttes CVR-nummer
- Gemmes i Supabase

#### Email Data
- Emails modtages via forwarding
- Grupperes i tråde
- Tilknyttes CVR-nummer
- Gemmes i Supabase

#### Dokumenter
- Uploades gennem CRM interface
- Konverteres til vector format
- Kategoriseres og gemmes
- Tilknyttes CVR-nummer

### 2. Data Processing

#### Backend Processing
- Modtager rå data fra alle kilder
- Konverterer tekst til vectors
- Analyserer indhold
- Genererer anbefalinger
- Beregner priser

#### Database Lagring
- Struktureret data i PostgreSQL
- Vector data i Supabase
- Relaterede data via CVR-nummer
- Versions styring af ændringer

### 3. Data Præsentation

#### CRM Interface
- Bruger logger ind på platformen
- Ser kun data for relevante CVR-numre
- Får præsenteret:
  - Chatbot historik
  - Email korrespondance
  - Uploadede dokumenter
  - Næste-skridt anbefalinger
  - Prisberegninger

## Hosting og Drift

### Frontend (CRM Interface)
- Hostet på Vercel/Netlify
- Tilgængelig 24/7
- Automatisk scaling
- SSL/HTTPS sikkerhed

### Backend API
- Hostet på DigitalOcean App Platform
- Automatisk restart ved fejl
- Load balancing
- Kontinuerlig monitorering

### Database
- Supabase cloud hosting
- Automatisk backup
- Høj tilgængelighed
- Skalerbar performance

## Sikkerhed

### Brugeradgang
- Sikker login process
- CVR-baseret adgangskontrol
- Krypteret dataforbindelse
- Session håndtering

### Data Sikkerhed
- Krypteret data transmission
- Sikker data lagring
- Backup med 24-timers roll-back
- Audit trail af ændringer

## Monitorering

### System Sundhed
- Real-time monitoring
- Performance tracking
- Fejl notifikationer
- Kapacitets overvågning

### Data Kvalitet
- Validering af indgående data
- Konsistens tjek
- Data integritets verifikation
- Quality metrics tracking