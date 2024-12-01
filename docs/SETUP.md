# Opsætning af Udviklingsmiljø

## Forudsætninger
- Python 3.8+ (allerede installeret)
- VS Code
- Git
- Supabase account

## Miljø Setup

### Virtual Environment
```bash
# Opret virtual environment i projekt mappen
python -m venv venv

# Aktiver virtual environment (på Mac/Linux)
source venv/bin/activate

# Installer nødvendige pakker
pip install -r requirements.txt
```

### Supabase Setup
1. Test Database
   - Opret en separat database i din Supabase instance
   - Navn: `kundedata_test`
   - Bruges til udvikling og test

2. Produktions Database
   - Navn: `kundedata_prod`
   - Kun til produktionsdata

### VS Code Setup
1. Anbefalede Extensions:
   - Python extension
   - Git extension

2. Debug Setup:
   - Simpel Python debug konfiguration
   - Kør projektet med breakpoints

## Daglig Udvikling

### Skift Mellem Test/Produktion
```bash
# Test miljø (brug test database)
export SUPABASE_DB=kundedata_test

# Produktion (brug produktions database)
export SUPABASE_DB=kundedata_prod
```

### Kør Systemet Lokalt
```bash
# Start systemet
python src/main.py
```

### Test Data
- Begrænset test datasæt
- Kør kun tests mod test databasen
- Roll-back mulighed indenfor 24 timer via Supabase

## Bemærkninger
- Hold udvikling simpel med fokus på funktionalitet
- Brug test databasen til udvikling
- Undgå at påvirke produktionsdata under udvikling