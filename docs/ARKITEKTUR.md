# System Arkitektur

## Overordnet Systemstruktur

### Komponenter
1. **Data Indsamling**
   - Chatbot Integration
   - Email Integration
   - Hjemmeside Data Indsamling
   - Kundespecifikke Dokumenter
     - Upload håndtering
     - Vektor konvertering
     - Dokumentklassificering

2. **Database Lag**
   - Supabase (eksisterende)
     - Kundesamtaler
     - Email korrespondance
     - Vektordata fra hjemmeside
     - Vektordata fra dokumenter
     - Vidensbase
     - Fælles kundenøgle (company_id) på tværs af alle datatyper

3. **Backend Services**
   - API-lag til datahåndtering
   - Forretningslogik
   - Pris-beregningsmodul
   - Proces-anbefalingsmodul
     - Analyse af chatbot interaktioner
     - Analyse af email korrespondance
     - Intelligent next-step forslag

4. **Frontend/CRM**
   - Brugergrænsflade til dataoversigt
   - Lead-håndtering
   - Prisberegning
   - Procesoverblik og anbefalinger
   - Dokumenthåndtering per kunde

## Dataflow
1. **Indsamling af Data**
   - Chatbot → Database
   - Email → Database
   - Hjemmeside → Vektor Database
   - Dokumenter → Vektor Database
   - Alt data tagges med company_id

2. **Data Processering**
   - Sammenkædning af al kundedata via company_id
   - Berigelse med hjemmesidedata
   - Dokumentanalyse og kategorisering
   - Prisberegning baseret på vidensbase
   - Procesanalyse og næste-skridt beregning

3. **Data Præsentation**
   - CRM visning af kundedata
   - Lead-scoring og prioritering
   - Handlingsforslag baseret på data
   - Samlet kundeoverblik med alle datakilder
   - Procesvejledning og anbefalinger

## Sikkerhed og Performance
- Sikker datahåndtering i Supabase
- Optimeret databasestruktur
- Caching hvor relevant
- API-sikkerhed
- Sikker dokumenthåndtering

## Skalerbarhed
- Modulær arkitektur
- Microservices-tilgang hvor relevant
- Mulighed for fremtidig udvidelse
- Skalerbar dokumenthåndtering

## Teknisk Stack
- Database: Supabase
- Backend: Python
- Frontend: (TBD - framework vælges senere)
- API: FastAPI eller Flask

## Udviklingsfaser
1. **Fase 1: Grundlæggende Setup**
   - Repository struktur
   - Basis dokumentation
   - Udviklings-miljø
   - Definition af fælles kundenøgle struktur

2. **Fase 2: Data Håndtering**
   - Database schema implementation
   - Basis API endpoints
   - Data validering
   - Dokument upload system

3. **Fase 3: Integration**
   - Chatbot integration
   - Email integration
   - Hjemmeside data integration
   - Dokument processering
   - Implementering af company_id på tværs af systemer

4. **Fase 4: Intelligent Processering**
   - Udvikling af prisberegningsmodul
   - Implementering af procesanalyse
   - Udvikling af anbefalingssystem
   - Integration af alle datakilder

5. **Fase 5: CRM Implementation**
   - Frontend udvikling
   - Lead-håndtering
   - Samlet kundeoverblik
   - Proces- og prisvisning

6. **Fase 6: Test og Optimering**
   - Performance tests
   - Sikkerhedsgennemgang
   - Brugertest
   - Optimering af anbefalinger