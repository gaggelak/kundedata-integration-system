# Onboarding og Konfiguration

## Oversigt
Dette dokument beskriver hvordan virksomhedskonfiguration håndteres direkte i CRM systemet.

## CRM Integration

### Placering i CRM
Konfigurationsmodulet er tilgængeligt via hovedmenuen i CRM systemet:

```
https://jeres-crm.dk/
  ├── /dashboard        # Hovedoversigt
  ├── /leads           # Lead håndtering
  ├── /configuration   # Konfiguration
      ├── /prices      # Priskonfiguration
      ├── /templates   # Pris skabeloner
      └── /history     # Ændringshistorik
```

### Navigation

#### Hovedmenu
```
+---------------------------+
|        CRM Menu           |
+---------------------------+
| ✓ Dashboard              |
| ✓ Leads                  |
| ✓ Kunder                 |
| ✓ Priser & Konfiguration |
| ✓ Rapporter              |
| ✓ Indstillinger          |
+---------------------------+
```

#### Pris & Konfigurations Sektion
```
+---------------------------+
| Priser & Konfiguration    |
+---------------------------+
| • Prisoversigt           |
| • Rediger Priser         |
| • Import/Export          |
| • Historik               |
| • Skabeloner             |
+---------------------------+
```

## Brugergrænseflade

### 1. Prisoversigt i CRM
```
+----------------------------------------+
|   Prisoversigt - [Virksomhedsnavn]     |
+----------------------------------------+
| [Rediger Priser] [Import] [Historik]   |
|                                        |
| Aktive Prislister:                     |
| • Materialer (Sidst opdateret: i dag)  |
| • Arbejdsløn (Sidst opdateret: 3/12)  |
| • Kørsel (Sidst opdateret: 1/12)      |
+----------------------------------------+
```

### 2. Pris Editor
```
+----------------------------------------+
|          Rediger Priser                |
+----------------------------------------+
| Kategori: [Materialer v]               |
|                                        |
| [Bulk Rediger] [Import] [Export]       |
|----------------------------------------|
| Varenr. | Beskrivelse | Enhed | Pris   |
|---------|-------------|--------|--------|
| M001    | [          ]|  stk   |[     ]|
| M002    | [          ]|  m2    |[     ]|
|----------------------------------------|
|    [Gem] [Forhåndsvis] [Annuller]      |
+----------------------------------------+
```

### 3. Import Funktion
```
+----------------------------------------+
|            Import Priser                |
+----------------------------------------+
| [Download Skabelon]                     |
|                                        |
| [Vælg Fil]  eller  Træk fil hertil     |
|                                        |
| [Start Import] [Valider Først]         |
+----------------------------------------+
```

### 4. Historik Visning
```
+----------------------------------------+
|      Prisændrings Historik             |
+----------------------------------------+
| Periode: [Seneste 30 dage v]           |
|                                        |
| Dato     | Type    | Ændring  | Bruger |
|----------|---------|-----------|--------|
| 1/12/24  | Manuel  | +3 priser | ANE   |
| 30/11/24 | Import  | Bulk      | JM    |
|                                        |
| [Sammenlign] [Gendan Version]          |
+----------------------------------------+
```

## Roller og Rettigheder

### Brugertyper i CRM
1. **Admin**
   - Fuld adgang til alle priser og konfigurationer
   - Kan godkende ændringer
   - Kan oprette nye brugere

2. **Pris Manager**
   - Kan redigere priser
   - Kan importere nye prislister
   - Kan se historik

3. **Bruger**
   - Kan se priser
   - Kan generere tilbud
   - Kan ikke redigere

## Workflow

### Prisændringer
1. Bruger initierer ændring i CRM
2. System validerer ændringer
3. Preview af konsekvenser
4. Godkendelse (hvis nødvendigt)
5. Automatisk aktivering

### Bulk Import
1. Download aktuel skabelon fra CRM
2. Udfyld ændringer i Excel
3. Upload via CRM interface
4. Validering og preview
5. Godkendelse og aktivering

## Support og Hjælp

### Indbygget Hjælp
- Kontekstbaserede tooltips
- Video guides tilgængelige direkte i CRM
- Step-by-step guides for komplekse opgaver

### Support
- Live chat support i CRM
- Direkte link til support email
- Telefonsupport via CRM dashboard

## Best Practices

### For Brugere
1. Gennemgå ændringer før aktivering
2. Brug bulk import til store ændringer
3. Dokumentér ændringer i kommentarfeltet
4. Tag backup før større ændringer

### For Administratorer
1. Opsæt notifikationer for prisændringer
2. Gennemgå historik regelmæssigt
3. Vedligehold priskategorier
4. Opdater skabeloner efter behov