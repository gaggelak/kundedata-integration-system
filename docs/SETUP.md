# Setup Guide

## Udvikling

### Forudsætninger
- Docker Desktop
- Python 3.11+
- Git
- Node.js (for frontend udvikling)

### Initial Setup

1. **Klon Repository**
```bash
git clone https://github.com/[organisation]/kundedata-integration-system.git
cd kundedata-integration-system
```

2. **Miljø Variabler**
Opret .env filer for forskellige miljøer:

`.env.development`:
```env
# Database
SUPABASE_URL=your_dev_supabase_url
SUPABASE_KEY=your_dev_supabase_key

# Webhook
WEBHOOK_SECRET=your_dev_webhook_secret

# Email
EMAIL_SERVER=your_dev_email_server
EMAIL_ADDRESS=your_dev_email_address
EMAIL_PASSWORD=your_dev_email_password
```

`.env.test`:
```env
# Tilsvarende struktur med test miljø værdier
```

`.env.production`:
```env
# Tilsvarende struktur med produktions værdier
```

3. **Docker Setup**

Start udviklings miljøet:
```bash
docker-compose -f docker-compose.dev.yml up --build
```

## Komponent Setup

### Backend
```bash
# Opret virtuel miljø
python -m venv venv
source venv/bin/activate  # eller .\venv\Scripts\activate på Windows

# Installér dependencies
pip install -r requirements.txt

# Start backend
python src/main.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Deployment

### Cloud Hosting Setup

1. **Frontend (CRM)**
- Deploy på Vercel eller Netlify
- Konfigurér miljø variabler
- Sæt custom domæne op hvis nødvendigt

2. **Backend Services**
- Deploy på Digital Ocean eller AWS ECS
- Konfigurér container registry
- Sæt auto-scaling op

3. **Email Processor**
- Deploy som separat service
- Konfigurér email credentials
- Sæt monitoring op

### Deployment Kommandoer

```bash
# Build og push Docker images
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml push

# Deploy til produktion
./deploy.sh production
```

## Test Miljø

### Setup af Test Database
1. Opret separat Supabase projekt for test
2. Kør migrations
3. Indlæs test data

### Kør Tests
```bash
# Enhedstests
python -m pytest tests/unit

# Integrationstests
python -m pytest tests/integration

# E2E tests
python -m pytest tests/e2e
```

## Monitoring

### Logs
- Backend logs gemmes i `/var/log/app/`
- Frontend logs via Vercel/Netlify dashboard
- Email processor logs i separat log system

### Metrics
- CPU/Memory usage via cloud provider
- API response tider
- Queue længder for email processing

## Fejlfinding

### Common Issues
1. Database Connection
```bash
# Test database forbindelse
python scripts/test_db_connection.py
```

2. Webhook Tests
```bash
# Test webhook endpoint
python scripts/test_webhook.py
```

3. Email Processing
```bash
# Test email forbindelse
python scripts/test_email.py
```

## Sikkerhedskopiering

### Database Backup
```bash
# Manuel backup
python scripts/backup_db.py

# Gendan backup
python scripts/restore_db.py [backup_file]
```

### Log Rotation
- Logs roteres dagligt
- Gemmes i 30 dage
- Komprimeres efter 7 dage

## Vedligeholdelse

### Opdateringer
```bash
# Opdater dependencies
pip install -r requirements.txt --upgrade

# Opdater Docker images
docker-compose pull
```

### Sundhedstjek
```bash
# Kør system sundhedstjek
python scripts/health_check.py
```