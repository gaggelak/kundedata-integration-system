# Onboarding og Konfiguration

[tidligere indhold bevares...]

## Brugergrænseflade Specifikation

### 1. Hovedmenu
```
+---------------------------+
|     Hovednavigation       |
+---------------------------+
| ✓ Dashboard              |
| ✓ Priskonfiguration       |
| ✓ Historik               |
| ✓ Support                |
| ✓ Indstillinger           |
+---------------------------+
```

### 2. Pris Dashboard
```
+------------------+------------------+
|   Aktive Priser  | Hurtig Statistik |
+------------------+------------------+
| • Materialer    | • Antal ændringer|
| • Arbejdsløn    | • Sidst opdateret|
| • Kørsel        | • Afvigelser     |
+------------------+------------------+
|      Seneste Ændringer           |
+----------------------------------+
| • Dato | Bruger | Type | Status   |
+----------------------------------+
```

### 3. Pris Editor

#### Materiale Priser
```
+----------------------------------------+
| Kategori: [Vælg Kategori v]            |
+----------------------------------------+
| Varenr. | Beskrivelse | Enhed | Pris   |
|---------|-------------|--------|---------||
| M001    | [          ]|  stk   |[      ]|
| M002    | [          ]|  m2    |[      ]|
+----------------------------------------+
    [Gem] [Forhåndsvis] [Annuller]
```

#### Arbejdsløn Konfiguration
```
+----------------------------------------+
| Medarbejdertype: [Vælg Type v]         |
+----------------------------------------+
| Timepris | Overtid | Weekend | Helligdag|
|----------|----------|----------|----------|
|[        ]|[        ]|[        ]|[        ]|
+----------------------------------------+
```

### 4. Import/Export Interface
```
+----------------------------------------+
|            Import Prisliste             |
+----------------------------------------+
| [Download Skabelon]                     |
|                                        |
| [Vælg Fil]  eller  Træk fil hertil     |
|                                        |
| Format: [ Excel v ]                    |
|                                        |
| [Start Import] [Valider Først]         |
+----------------------------------------+
```

### 5. Historik og Versionering
```
+----------------------------------------+
|            Pris Historik                |
+----------------------------------------+
| Dato     | Version | Ændringer  | Bruger |
|----------|---------|------------|--------|
| 01-12-24 | 2.1     | +3 priser  | ANE   |
| 30-11-24 | 2.0     | Ny struktur| JM    |
+----------------------------------------+
    [Sammenlign] [Gendan] [Eksporter]
```

### 6. Valideringsvisning
```
+----------------------------------------+
|         Validering af Ændringer         |
+----------------------------------------+
| ⚠ 3 advarsler fundet:                 |
| • Pris M001 ændret med mere end 20%   |
| • Ny kategori tilføjet                |
| • 2 varer markeret som udgået         |
|                                        |
| [Godkend Alligevel] [Rediger] [Afbryd] |
+----------------------------------------+
```

### 7. Notifikationscenter
```
+----------------------------------------+
|           Notifikationer                |
+----------------------------------------+
| • Nye priser awaiting review           |
| • Bulk import completed                |
| • 3 price validation warnings          |
|                                        |
| [Markér Alle Som Læst] [Indstillinger]  |
+----------------------------------------+
```

### 8. Support Integration
```
+----------------------------------------+
|              Support                    |
+----------------------------------------+
|    [Start Chat] [Book Møde]            |
|                                        |
| Ofte Stillede Spørgsmål:               |
| • Hvordan importerer jeg priser?       |
| • Hvordan håndterer jeg rabatter?     |
| • Hvordan validerer jeg ændringer?    |
+----------------------------------------+
```

### 9. Mobile Responsive Design
```
// Mobil Layout
+----------------------+
|    ☰ Menu          |
+----------------------+
| Hurtig Adgang        |
| • Se Priser         |
| • Godkend Ændringer |
| • Support           |
+----------------------+
```

### 10. Kontekstafhjælpig Vejledning
- Hover tooltips med forklaringer
- Step-by-step guides for komplekse opgaver
- Video tutorials tilgængelige ved [?] ikoner
- Intelligent fejlmeddelelser med løsningsforslag

### 11. Keyboard Shortcuts
```
+----------------------------------------+
|           Keyboard Shortcuts            |
+----------------------------------------+
| Ctrl + S    : Gem ændringer            |
| Ctrl + Z    : Fortryd                  |
| Ctrl + F    : Søg                      |
| Ctrl + P    : Forhåndsvis              |
+----------------------------------------+
```

### 12. Brugerpræferencer
```
+----------------------------------------+
|           Præferencer                   |
+----------------------------------------+
| ☐ Vis bekræftelsesdialoger            |
| ☐ Automatisk gem                      |
| ☐ Email notifikationer                |
| ☐ Dark mode                           |
+----------------------------------------+
```

## Best Practices for Brugergrænseflade

### Generelle Principper
1. Konsistent layout og navigation
2. Klare og synlige handlingsknapper
3. Trinvis validering af input
4. Tydelig feedback på handlinger

### Fejlhåndtering
1. Proaktiv validering (under indtastning)
2. Klare fejlmeddelelser
3. Foreslåede løsninger
4. Mulighed for at fortryde

### Performance
1. Lazy loading af data
2. Caching af hyppigt brugte data
3. Optimeret for hurtig respons
4. Progress indikatorer ved længere operationer