# Kravspecifikation

## Projektets Formål
Systemet skal modtage, analysere og præsentere kundedata fra forskellige kilder i et samlet CRM-interface. Formålet er at give et komplet overblik over kundedialog og muliggøre kvalificerede beslutninger om næste skridt samt prissætning.

## Hovedkomponenter

### 1. Data Modtagelse
Systemet skal modtage data fra følgende eksterne kilder:
- Chatbot samtaler (via webhook fra Wotnot)
- Email korrespondance (via email forwarding)
- Kundespecifikke dokumenter (via upload)
- Hjemmeside data (via crawling)

**Vigtigt:** Systemet bygger ikke selve chatbotten eller email-systemet, men modtager kun data fra disse.

### 2. Data Analyse og Strukturering
- Gem al data i Supabase database
- Konverter relevant tekst til vector format
- Sammenkæd al data via CVR-nummer
- Sikr nem søgning i historisk data

### 3. Intelligent Analyse
Systemet skal kunne:
- Analysere chatbot samtaler og emails
- Generere konkrete forslag til næste skridt
- Beregne priser baseret på tilgængelig data
- Identificere mønstre og tendenser

### 4. CRM Interface
Brugerflåden skal indeholde:
- Board/swimlane view til lead tracking
- Samlet overblik over al kundekommunikation
- Præsentation af næste-skridt anbefalinger
- Visning af prisberegninger

## Tekniske Krav

### Database
- Brug af Supabase som primær database
- Vector storage til tekstanalyse
- Separate test- og produktionsmiljøer

### Integration
- Webhook endpoint til chatbot data
- Email forwarding system
- Dokument upload håndtering
- Hjemmeside crawler

### Sikkerhed
- CVR-baseret adgangsbegrænsning
- Sikker håndtering af kundedata
- Backup med 24-timers roll-back

### Skalerbarhed
- Håndtering af voksende datamængder
- Effektiv vector søgning
- Optimeret databasestruktur

## Afgrænsninger

Systemet inkluderer IKKE:
- Udvikling af chatbot
- Email system implementation
- Direkte kundekommmunikation
- CMS funktionalitet

## Brugerroller
- Brugere kan kun se data for deres egne kunder (CVR-baseret)
- Forskellige brugerroller med varierende adgangsniveauer

## Fremtidige Udvidelser
- Mulighed for direkte kommunikation fra CRM
- Udvidet GDPR compliance
- Automatisk audit trail
- Advanceret logging
