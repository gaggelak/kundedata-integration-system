# Prisberegning

## Overordnet Struktur

Prisberegningssystemet håndterer forskellige komponenter og kategorier for at komme frem til en samlet pris.

### Pris Komponenter
1. Materialer
   - Priser fra prisliste dokumenter
   - Kategoriseret efter type
   - Mængde/antal håndtering

2. Kørsel
   - Fast takst eller kilometerbaseret
   - Zoneinddelinger hvis relevant

3. Arbejdsløn
   - Timepriser
   - Forskellige medarbejderkategorier
   - Estimeret tidsforbrug

## Beregningsprocess

### 1. Data Indsamling
- Indhent relevante prisdokumenter for kunde (via CVR)
- Identificer relevante priskategorier
- Tjek for kundespecifikke aftaler

### 2. Beregnings Steps
1. **Basis Materialeberegning**
   - Identificér nødvendige materialer
   - Beregn materialepris baseret på mængde
   - Summér materialeomkostninger

2. **Arbejdslønsberegning**
   - Estimér arbejdstimer
   - Anvend relevante timepriser
   - Beregn samlet arbejdsløn

3. **Kørselsberegning**
   - Medtag relevante kørselsomkostninger
   - Beregn baseret på afstand/zone

4. **Samlet Beregning**
   - Summér alle komponenter
   - Tilføj eventuelt overhead
   - Beregn eventuelle rabatter

## Prisforklaring og Transparens

### Kundevendt Forklaring
- Detaljeret nedbrydning af hver priskomponent
- Visuelle elementer (grafer/diagrammer) der viser prisfordeling
- Forklaring i almindeligt sprog for hver delberegning
- Sammenligning med standardpriser hvor relevant

### Teknisk Sporbarhed
- Log af alle delberegninger
- Reference til anvendte prisdokumenter
- Timestamp for hver delberegning
- Versionering af anvendte prisdata

### Beregningsdetaljer
- Specificering af anvendte formler
- Mellemregninger for hver komponent
- Dokumentation af eventuelle særlige forhold
- Markering af eventuelle estimater eller antagelser

## Prisdata Håndtering

### Prisdokumenter
- Struktureret format for prislister
- Versionering af priser
- Gyldighedsperioder

### Kategorisering
- Materiale kategorier
- Arbejdstype kategorier
- Kørselstyper

## Output

### Prisspecifikation
- Detaljeret nedbrydning af pris
- Separate linjer for hver komponent
- Tydelig visning af delpriser
- Forklarende tekst for hver komponent

### Dokumentation
- Hvilke prislister der er anvendt
- Hvilke beregninger der er foretaget
- Timestamp for beregningen
- Version af anvendte priser
- Forklaringer på eventuelle særlige forhold

## Vedligeholdelse

### Opdatering af Priser
- Process for opdatering af prislister
- Håndtering af prisversioner
- Historik over prisændringer

### Kvalitetssikring
- Validering af prisberegninger
- Kontrol af priskomponenter
- Sammenligning med historiske priser

## Fejlhåndtering

### Manglende Data
- Håndtering af manglende priser
- Fallback værdier
- Notifikation om manglende data

### Validering
- Kontrol af beregningsresultater
- Advarsler ved usædvanlige værdier
- Logging af fejl og advarsler

## Rapportering

### Prishistorik
- Gemme alle prisberegninger
- Mulighed for at se tidligere beregninger
- Analyse af prisændringer over tid
- Forklaring af prisudvikling

### Statistik
- Gennemsnitspriser per kategori
- Identifikation af prismønstre
- Afvigelsesrapporter
- Forklaringer på statistiske afvigelser