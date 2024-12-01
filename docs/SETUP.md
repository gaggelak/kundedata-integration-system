# Opsætning af Udviklingsmiljø

## Forudsætninger
- Python 3.8+
- Docker og Docker Compose
- PostgreSQL
- Git

## Trin for Trin Guide

### 1. Kloning af Repository
```bash
git clone https://github.com/gaggelak/kundedata-integration-system.git
cd kundedata-integration-system
```

### 2. Miljøvariabler
Kopier `.env.example` til `.env` og udfyld:
- DATABASE_URL
- SUPABASE_URL
- SUPABASE_KEY
- EMAIL_SERVER_CONFIG
- OPENAI_API_KEY

### 3. Opsætning af Database
```bash
# Start PostgreSQL og Supabase
docker-compose up -d database vectordb

# Kør migrationer
python manage.py migrate
```

### 4. Installation af Afhængigheder
```bash
python -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 5. Kør Tests
```bash
pytest
```

### 6. Start Udviklingsserver
```bash
python manage.py runserver
```

## Grenstruktur
- `main` - Produktionskode
- `udvikling` - Primær udviklingsgren
- `funktion/*` - Funktionsgrene (f.eks. `funktion/chatbot-integration`)

## Kodestil
- PEP 8 standarder
- Dokumentation på dansk
- Variabelnavne på dansk

## Docker Development
Se `docker/README.md` for detaljer om Docker setup.

## Hjælp og Support
Kontakt teamet på [intern Teams kanal] eller opret et issue på GitHub.