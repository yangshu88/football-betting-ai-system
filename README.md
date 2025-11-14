# Football Betting AI System

## Objective
Create a modular, scalable AI-driven football betting system capable of:
- Ingesting fixture and stats data for multiple bet types daily
- Calculating Smart Bets and Golden Bets each morning
- Updating odds frequently and dynamically recalculating Value Bets
- Serving cached AI predictions with explanations for fast user interaction

## System Architecture

### Modules
- **data-ingestion/** — Fixture and stats API fetcher
- **smart-bets-ai/** — AI model calculating Smart Bets
- **golden-bets-ai/** — AI model for Golden Bets
- **odds-updater/** — Odds API polling and storage
- **value-bets-ai/** — Dynamic Value Bet recalculation engine
- **summary-generator/** — Generates explanations for AI bets
- **user-api/** — Serves cached results to frontend/UI

## Development Strategy

### Stepwise Module Building
Build and test each module independently.

### Mock Data & APIs
Use mock data/services to simulate dependencies early in development.

### Integration Phase
Once individual modules are stable, connect them via shared data stores (databases, caches) and event triggers.

### Testing
Emphasize unit tests, integration tests, and end-to-end tests.

### Documentation
Maintain clear docs for each module and the entire system.

## Next Steps
1. Start by building data-ingestion module to fetch and store daily fixture and stats data
2. Confirm data schema and storage approach
3. Then proceed with AI model modules (smart-bets-ai and golden-bets-ai) using the ingested data
