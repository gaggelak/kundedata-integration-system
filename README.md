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

## Installation og Opsætning

### 1. Klargør Udviklingsmiljø
```bash
# Installer systemafhængigheder (Ubuntu/Debian)
sudo apt update
sudo apt install python3.8 python3.8-venv python3-pip postgresql docker docker-compose

# Eller på macOS med Homebrew
brew install python@3.8 postgresql docker docker-compose
```

### 2. Klon Repository
```bash
git clone https://github.com/gaggelak/kundedata-integration-system.git
cd kundedata-integration-system
```

### 3. Opsæt Python Miljø
```bash
# Opret og aktiver virtual environment
python3.8 -m venv venv
source venv/bin/activate  # På Windows: .\venv\Scripts\activate

# Installer afhængigheder
pip install -r requirements.txt
```

### 4. Miljøvariabler
```bash
# Kopier example fil
cp .env.example .env

# Rediger .env med dine værdier:
# - DATABASE_URL=postgresql://user:password@localhost:5432/kundedata
# - SUPABASE_URL=din-supabase-url
# - SUPABASE_KEY=din-supabase-key
# - EMAIL_SERVER=smtp.example.com
# - EMAIL_PORT=587
# - EMAIL_USER=user@example.com
# - EMAIL_PASSWORD=password
```

### 5. Database Opsætning
```bash
# Start PostgreSQL og Supabase med Docker
docker-compose up -d database vectordb

# Kør database migrationer
python manage.py migrate
```

### 6. Start Udviklings-server
```bash
# Start backend server
python manage.py runserver

# I en ny terminal, start frontend udviklings-server
cd frontend
npm install
npm start
```

### Verificer Installation
1. Åbn http://localhost:8000/admin i en browser
2. Log ind med standard admin credentials (admin/admin)
3. Test at webhook endpoint er tilgængeligt: http://localhost:8000/api/webhook

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

## Udviklingsstatus
- [x] Initial repository oprettet
- [ ] Database skema design
- [ ] Webhook endpoint implementering
- [ ] Email modtagelse setup
- [ ] Analyse implementering
- [ ] Frontend udvikling

## Fejlfinding
### Almindelige Problemer
1. **Database Connection Error**  
   Tjek at PostgreSQL kører og at DATABASE_URL er korrekt i .env

2. **Supabase Connection Error**  
   Verificer SUPABASE_URL og SUPABASE_KEY i .env

3. **Missing Dependencies**  
   Kør `pip install -r requirements.txt` igen

4. **Port Already in Use**  
   Tjek og stop andre services der bruger port 8000

## Yderligere Information
Se `/docs` mappen for detaljeret dokumentation om:
- System arkitektur
- API endpoints
- Database schema
- Udviklings-workflow
- Sikkerhed

## Licens
Dette projekt er under udvikling og licensbetingelser vil blive tilføjet senere.