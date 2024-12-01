# Database Struktur

## Oversigt
Dette dokument beskriver den komplette database struktur for kundedata integration systemet.

## Database Miljøer

### Produktion
- Database: kundedata_prod
- Forbindelse via Supabase
- Fuld backup dagligt
- 24-timers point-in-time recovery

### Test
- Database: kundedata_test
- Isoleret testmiljø
- Daglig reset mulighed
- Test data generation

## Company ID (CVR) Struktur
Systemet bruger CVR-nummer som den primære nøgle til at identificere virksomheder på tværs af alle tabeller.

## Tabeller

### users
- id (primary key)
- email
- password_hash
- created_at
- last_login
- role (admin, user, etc.)
- active

### user_companies
- user_id (foreign key)
- cvr (foreign key)
- access_level
- granted_at
- granted_by

### companies
- cvr (primary key)
- navn
- oprettet_dato
- sidst_opdateret
- status (active, inactive)

### chatbot_conversations
- id (primary key)
- cvr (foreign key)
- raw_conversation (rå samtale data)
- conversation_vector (vector embedding)
- created_at
- metadata (JSON med ekstra data fra chatbot)

### email_threads
- id (primary key)
- cvr (foreign key)
- thread_subject
- raw_thread (komplet tråd)
- thread_vector (vector embedding af hele tråden)
- attachments_links (array af links)
- created_at
- last_updated

### document_categories
- id (primary key)
- navn
- beskrivelse
- active

### documents
- id (primary key)
- cvr (foreign key)
- category_id (foreign key)
- document_name
- raw_content
- vector_content
- uploaded_at
- last_updated
- uploaded_by (foreign key til users)
- version

### process_steps
- id (primary key)
- cvr (foreign key)
- recommendation_text
- confidence_score (scoring for prioritering)
- based_on_conversation_id (foreign key til chatbot_conversations)
- based_on_thread_id (foreign key til email_threads)
- created_at
- status (fx active, completed, skipped)
- created_by (foreign key til users)

### price_calculations
- id (primary key)
- cvr (foreign key)
- final_price
- calculation_date
- data_sources (JSON array med henvisninger til brugte dokumenter/samtaler)
- calculation_parameters (JSON med detaljer om beregningen)
- partial_results (JSON med delresultater for troubleshooting)
- version (for at tracke ændringer i beregningslogik)
- created_by (foreign key til users)

### system_logs
- id (primary key)
- timestamp
- event_type
- user_id (foreign key, nullable)
- cvr (foreign key, nullable)
- details (JSON)
- severity (info, warning, error)

## Indeksering

### Primære Indekser
- Alle foreign keys er indekseret
- Vector embeddings er indekseret for hurtig similarity search
- Tidsstempler er indekseret for performance ved datofiltreringer
- Email subjects for hurtig søgning
- Dokumentnavne og kategorier

### Composite Indekser
- (cvr, created_at) for tidsbaserede forespørgsler per virksomhed
- (user_id, cvr) for hurtig adgangskontrol
- (event_type, timestamp) for effektiv log søgning

## Vector Håndtering
- Alle vector embeddings gemmes i et format kompatibelt med Supabase vector extensions
- Optimal dimension af vectors bestemmes ved implementation
- Effektiv søgning via pgvector extension
- Automatisk indeksering af nye vectors

## Relationer
- Alle tabeller er relationelt forbundet via CVR nummer
- Brugeradgang styres via user_companies tabellen
- price_calculations refererer til relevante documents og conversations
- process_steps kan referere til både samtaler og email tråde

## Skalerbarhed

### Data Partitionering
- Store tabeller partitioneres efter dato
- Separate partitioner for historisk data
- Effektiv arkivering af gamle data

### Performance
- Materialized views for komplekse rapporter
- Optimal indeksering for typiske queries
- Caching af hyppigt anvendt data

### Vedligeholdelse
- Automatisk vacuum og analyze
- Regulær reindeksering
- Statistik opdatering

## Backup og Recovery

### Backup Strategi
- Daglig fuld backup
- Kontinuerlig WAL arkivering
- Geografisk replikering

### Recovery
- Point-in-time recovery mulighed
- Automatisk failover
- Disaster recovery plan

## Sikkerhed

### Adgangskontrol
- Row Level Security (RLS) via CVR
- Kryptering af følsomme data
- Audit logging af alle ændringer

### Monitoring
- Performance metrics
- Query statistik
- Resource forbrug
- Sikkerhedsadvarsler