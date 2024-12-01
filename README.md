# Kundedata Integration System

## Projektoversigt
Dette system modtager og analyserer kundedata fra forskellige kilder:
- Chatbot samtalehistorik (via webhook)
- Email korrespondance (via email forwarding)
- Hjemmeside data
- Vidensbase dokumenter

Systemet analyserer data og genererer anbefalinger til næste skridt samt prisberegninger.

## Systemkrav
- Python 3.8+
- PostgreSQL
- Supabase (til vektor database)
- Docker (til deployment)

## Projektstruktur
```
kundedata-integration-system/
├── src/                     # Kildekode
│   ├── api/                # API endpoints
│   ├── database/          # Database skemaer og migrations
│   ├── services/         # Forretningslogik
│   └── utils/            # Hjælpefunktioner
├── tests/                  # Test filer
├── docs/                   # Dokumentation
└── docker/                # Docker konfiguration
```

## Installation
*Detaljeret installationsvejledning tilføjes senere*

## Udviklingsstatus
- [x] Initial repository oprettet
- [ ] Database skema design
- [ ] Webhook endpoint implementering
- [ ] Email modtagelse setup
- [ ] Analyse implementering
- [ ] Frontend udvikling

## Licens
Dette projekt er under udvikling og licensbetingelser vil blive tilføjet senere.