# Onboarding og Konfiguration

## Oversigt
Dette dokument beskriver processen for onboarding af nye virksomheder og håndtering af deres priskonfiguration gennem selvbetjening.

## Initial Onboarding

### 1. Oprettelse af Virksomhed
- Registrering af CVR nummer
- Oprettelse af virksomhedsprofil
- Tildeling af brugeradgang

### 2. Basis Konfiguration (Udføres af Admin)
- Opsætning af webhook integration
- Konfiguration af email forwarding
- Aktivering af relevante moduler

### 3. Priskonfiguration
- Upload af initiale prislister
- Konfiguration af beregningsregler
- Test af prisberegninger

## Selvbetjenings Portal

### Pris Administration

#### Visning af Priser
- Oversigt over alle aktive priser
- Historik over prisændringer
- Filtreringsmuligheder
- Eksport funktion

#### Opdatering af Priser
- Brugervenlig editor interface
- Mulighed for bulk updates via Excel import
- Preview af ændringer før aktivering
- Versionering af prislister

#### Notifikationer
- Automatisk notifikation til admin ved ændringer
- Bekræftelsesmail til virksomheden
- Varsling ved større prisændringer

### Sikkerhed og Kontrol

#### Brugeradgang
- Forskellige adgangsniveauer
- To-faktor autentificering for prisændringer
- Audit log af alle ændringer

#### Validering
- Automatisk kontrol af prisformater
- Advarsler ved usædvanlige ændringer
- Sammenligning med historiske priser

## Support Proces

### Rådgivning
- Mulighed for at booke online rådgivning
- Support chat i selvbetjeningsportalen
- Video guides til almindelige opgaver

### Problemhåndtering
- Direkte support hotline
- Fejlrettelse af forkerte indtastninger
- Gendan tidligere versioner hvis nødvendigt

## Interface Design

### Selvbetjenings Dashboard
```
+------------------------+
|   Virksomhedsoversigt   |
+------------------------+
| - Aktive prislister    |
| - Seneste ændringer    |
| - Ventende godkendelser|
+------------------------+

+------------------------+
|    Pris Administration |
+------------------------+
| - Rediger priser       |
| - Import/Export        |
| - Historik             |
+------------------------+

+------------------------+
|      Support           |
+------------------------+
| - Book rådgivning      |
| - Support chat         |
| - Dokumentation        |
+------------------------+
```

## API Integration

### Endpoints
- `GET /api/prices/{cvr}` - Hent aktuelle priser
- `PUT /api/prices/{cvr}` - Opdater priser
- `GET /api/prices/{cvr}/history` - Pris historik
- `POST /api/prices/{cvr}/validate` - Valider prisændringer

### Webhooks
- Notifikation ved prisændringer
- Validering af nye priser
- Audit log events

## Vedligeholdelse

### Automatisk Vedligeholdelse
- Daglig backup af priskonfigurationer
- Periodevise validerings checks
- Rensning af forældede prisdata

### Manuel Vedligeholdelse
- Regulær gennemgang af prisstrukturer
- Optimering af beregningsregler
- Opdatering af valideringsregler

## Best Practices

### For Virksomheder
1. Gennemgå priser regulært
2. Test ændringer før aktivering
3. Hold dokumentation opdateret
4. Brug versionering aktivt

### For Administratorer
1. Overvåg prisændringer
2. Følg op på usædvanlige mønstre
3. Vedligehold valideringsregler
4. Opdater support materiale