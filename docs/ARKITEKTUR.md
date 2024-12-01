# System Arkitektur

## Overordnet Systemstruktur

### Komponenter
1. **Data Modtagelse**
   - Webhook endpoint for chatbot data
   - Email forwarding system
   - Hjemmeside data indsamling
   - Dokument upload håndtering

2. **Database Lag**
   - Supabase (eksisterende)
     - Kundesamtaler fra chatbot
     - Email korrespondance
     - Vektordata fra hjemmeside
     - Vektordata fra dokumenter
     - Fælles kundenøgle (CVR)

3. **Analyse Services**
   - Data processering
   - Anbefalingsmodul
   - Pris-beregningsmodul

4. **CRM Interface**
   - Visning af lead data
   - Procesanbefalinger
   - Prisberegning

## Dataflow
1. **Data Modtagelse**
   - Modtag chatbot data via webhook
   - Modtag emails via forwarding
   - Indsaml hjemmeside data
   - Håndter dokumentupload

2. **Data Processering**
   - Vector konvertering af al data
   - Analyse af kundeinteraktioner
   - Prisberegning baseret på data

3. **CRM Præsentation**
   - Samlet lead overblik
   - Anbefalinger til næste skridt
   - Prisberegning og estimater

## Sikkerhed og Performance
- Sikker datahåndtering
- Optimeret søgning i vector data
- Effektiv webhook håndtering
- Sikker dokumenthåndtering

## Skalerbarhed
- Modulær arkitektur
- Optimeret datahåndtering
- Skalerbar analyse

## Teknisk Stack
- Database: Supabase
- Backend: Python
- Frontend: (TBD - framework vælges senere)
- API: FastAPI eller Flask

## Udviklingsfaser
1. **Fase 1: Grundlæggende Setup**
   - Repository struktur
   - Database setup
   - Webhook endpoints

2. **Fase 2: Data Håndtering**
   - Implementering af data modtagelse
   - Vector konvertering
   - Data validering

3. **Fase 3: Analyse**
   - Implementation af analysemodul
   - Prisberegning
   - Anbefalingssystem

4. **Fase 4: CRM Interface**
   - Frontend udvikling
   - Lead visning
   - Anbefalingsvisning

5. **Fase 5: Test og Optimering**
   - Performance tests
   - Sikkerhedsgennemgang
   - Brugertest