# Setup Guide

## Udvikling

### Forudsætninger
- Python 3.8+ (allerede installeret)
- VS Code med extensions:
  - Python
  - Git
  - REST Client (valgfri)
- Git
- Supabase account

### Lokal Udvikling

#### 1. Repository Setup
```bash
# Klon repository
git clone https://github.com/[organisation]/kundedata-integration-system.git
cd kundedata-integration-system

# Opret og aktiver virtual environment
python -m venv venv
source venv/bin/activate  # På Mac/Linux

# Installér afhængigheder
pip install -r requirements.txt
```

#### 2. Miljøvariabler
Kopiér `.env.example` til `.env` og udfyld:
```env
# Supabase
SUPABASE_URL=din_supabase_url
SUPABASE_KEY=din_supabase_key

# Database valg
SUPABASE_DB=kundedata_test  # eller kundedata_prod

# Email config
EMAIL_SERVER=smtp.example.com
EMAIL_PORT=587
EMAIL_USERNAME=user@example.com
EMAIL_PASSWORD=password
```

#### 3. Database Setup
1. Opret test database i Supabase dashboard
2. Opret produktions database i Supabase dashboard
3. Kør basis database setup via Supabase interface

#### 4. Kør Lokalt
```bash
# Start udviklings-server
python src/main.py
```

## Deployment

### Frontend (CRM Interface)

#### Vercel Setup
1. Forkæl frontend repository til din GitHub konto
2. Opret nyt projekt på Vercel
3. Vælg repository og konfigurér build settings
4. Tilføj miljøvariabler

#### Netlify Alternativ
1. Forkæl frontend repository
2. Opret nyt site på Netlify
3. Konfigurér build settings
4. Tilføj miljøvariabler

### Backend (API)

#### DigitalOcean App Platform
1. Forkæl backend repository
2. Opret ny app på DigitalOcean
3. Vælg repository og konfigurér
4. Tilføj miljøvariabler
5. Deploy

### Monitoring

#### Sundhedstjek
- Backend status: `https://api.example.com/health`
- Database connection: `https://api.example.com/health/db`
- Email system: `https://api.example.com/health/email`

#### Logs
- Backend logs via DigitalOcean dashboard
- Frontend logs via Vercel/Netlify dashboard
- Database logs via Supabase dashboard

## Vedligeholdelse

### Database Backup
- Automatisk daglig backup via Supabase
- 24-timers roll-back mulighed
- Separat test og produktion

### Opdateringer
```bash
# Opdater dependencies
pip install -r requirements.txt --upgrade

# Commit ændringer
git add requirements.txt
git commit -m "Opdaterer dependencies"
git push
```

## Fejlfinding

### Almindelige Problemer

1. **Database Connection Error**
   - Tjek SUPABASE_URL og SUPABASE_KEY i .env
   - Verificer database eksisterer
   - Tjek netværksforbindelse

2. **Email System Fejl**
   - Tjek email credentials
   - Verificer SMTP server tilgængelighed
   - Tjek firewall indstillinger

3. **Webhook Fejl**
   - Verificer endpoint URL
   - Tjek request format
   - Gennemgå webhook logs
