# Integrations Guide

## Oversigt
Dette dokument beskriver hvordan systemet integrerer med forskellige datakilder.

## 1. Chatbot Webhook Integration

### Endpoint
- Wotnot webhook URL format: `https://hooks.wotnot.io/incoming/webhook/{webhook_id}`
- Implementering af webhook endpoint til at modtage data
- Authentication detaljer implementeres når tilgængelige

### Data Håndtering
- Modtag webhook payload
- Validering af data format
- Gem rå samtale data
- Konverter til vector format
- Tilknyt CVR nummer

## 2. Email Integration

### Email Forwarding Setup
- Dedikeret email adresse til at modtage forwards
- Email parsing system
- Tråd-identificering baseret på subject og references

### Data Håndtering
- Parse email indhold og metadata
- Identificer og grupper email tråde
- Gem rå email data
- Konverter til vector format
- Tilknyt CVR nummer

## 3. Hjemmeside Crawler

### Crawling Specifikationer
- Månedlig crawling af kunders hjemmesider
- Inkrementel opdatering (kun nye/ændrede sider)
- Fokus på tekstindhold fra alle sider

### Data Håndtering
- Crawl alle tekstsider
- Rens og strukturer tekst data
- Konverter til vector format
- Gem med relation til CVR
- Marker timestamp for seneste crawl

## 4. Dokument Upload

### Upload Specifikationer
- Tilladte filformater:
  - .jpg
  - .img
  - .pdf
  - .docx
  - .xlsx
- Maksimal filstørrelse: 10 MB

### Metadata Håndtering
Følgende metadata gemmes for hvert dokument:
- Upload tidspunkt
- Dokument kategori
- Upload bruger
- Sidst ændret tidspunkt
- Version nummer
- Original filnavn
- Checksum for duplicate detection

### Data Håndtering
- Validering af filformat og størrelse
- Virus scanning
- Metadata udtrak
- Konvertering til vector format
- Tilknytning til CVR

## 5. Vector Konvertering

### Proces for alle datatyper
1. Udtrak relevant tekst
2. Rens og normaliser data
3. Generer vector embedding
4. Gem i Supabase vector database

### Optimering
- Batch processing hvor muligt
- Caching af ofte brugte vectors
- Inkrementel opdatering

## 6. Fejlhåndtering

### Webhook Fejl
- Retry mekanisme for fejlede webhook calls
- Logging af fejlede requests
- Alerting ved gentagne fejl

### Email Fejl
- Håndtering af fejlformatterede emails
- Backup af rå emails
- Fejlrapportering ved parsing problemer

### Crawler Fejl
- Håndtering af utilgængelige sites
- Logging af crawling fejl
- Retry mekanisme

### Upload Fejl
- Validering feedback til bruger
- Logging af fejlede uploads
- Cleanup af fejlede uploads

## 7. Monitorering

### Performance
- Responstider for hver integrationspunkt
- Success/fejl rates
- Data kvalitet metrics

### Alerts
- Kritiske integrationsfejl
- Kapacitets advarsler
- Sikkerhedshændelser