# Database Struktur

## Oversigt
Dette dokument beskriver den komplette database struktur for kundedata integration systemet.

## Company ID (CVR) Struktur
Systemet bruger CVR-nummer som den primære nøgle til at identificere virksomheder på tværs af alle tabeller.

## Tabeller

### companies
- cvr (primary key)
- navn
- oprettet_dato
- sidst_opdateret

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

### documents
- id (primary key)
- cvr (foreign key)
- category_id (foreign key)
- document_name
- raw_content
- vector_content
- uploaded_at
- last_updated

### process_steps
- id (primary key)
- cvr (foreign key)
- recommendation_text
- confidence_score (scoring for prioritering)
- based_on_conversation_id (foreign key til chatbot_conversations)
- based_on_thread_id (foreign key til email_threads)
- created_at
- status (fx active, completed, skipped)

### price_calculations
- id (primary key)
- cvr (foreign key)
- final_price
- calculation_date
- data_sources (JSON array med henvisninger til brugte dokumenter/samtaler)
- calculation_parameters (JSON med detaljer om beregningen)
- partial_results (JSON med delresultater for troubleshooting)
- version (for at tracke ændringer i beregningslogik)

## Indeksering
- Alle foreign keys er indekseret
- Vector embeddings er indekseret for hurtig similarity search
- Tidsstempler er indekseret for performance ved datofiltreringer

## Vector Håndtering
- Alle vector embeddings gemmes i et format kompatibelt med Supabase vector extensions
- Optimal dimension af vectors bestemmes ved implementation

## Relationer
- Alle tabeller er relationelt forbundet via CVR nummer
- price_calculations refererer til relevante documents og conversations
- process_steps kan referere til både samtaler og email tråde

## Skalerbarhed
- Tabeller er designet til at håndtere store mængder data
- Vector søgning er optimeret gennem Supabase
- Metadata og delresultater gemmes i JSON format for fleksibilitet

## Vedligeholdelse
- Alle tabeller inkluderer timestamps for audit trail
- Version tracking på prisberegninger for at spøre ændringer
- Mulighed for soft delete på alle relevante tabeller