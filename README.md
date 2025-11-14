# Football Betting AI System

## Overview
This project is the **AI prediction engine** - the intelligent core that analyzes football fixtures and generates betting predictions. It receives data from your main app, runs AI models, and returns Smart Bets, Golden Bets, and Value Bets with explanations.

**This system is NOT the full betting app** - it's the AI brain that powers predictions. Your main app handles the frontend, data ingestion, user management, and payments.

## What This System Does

✅ **Accepts data** from your app (fixtures, stats, odds)  
✅ **Runs AI models** to generate predictions  
✅ **Calculates three bet types:**
- **Smart Bets:** Pure AI probabilities (ignoring odds)
- **Golden Bets:** High-confidence strategic bets
- **Value Bets:** Dynamic recalculations comparing AI probability vs market odds

✅ **Generates explanations** for why bets were selected  
✅ **Exposes API endpoints** for your app to query  
✅ **Caches predictions** for fast response times

## What This System Does NOT Do

❌ Frontend application  
❌ Data scraping from external sources  
❌ User authentication  
❌ Payment processing

## Architecture
The system is composed of several interconnected modules:

### **data-ingestion/**
Receives and validates fixture data, team stats, and odds from your main app.

### **smart-bets-ai/**
Calculates pure probabilistic predictions for each match using AI models (XGBoost/LightGBM baseline).

### **golden-bets-ai/**
Identifies high-confidence bets using confidence thresholds and ensemble agreement metrics.

### **odds-updater/**
Processes odds updates from your app for real-time value calculations.

### **value-bets-ai/**
Dynamically recalculates value bets by comparing AI probabilities vs implied odds probabilities.

### **summary-generator/**
Creates human-readable AI explanations for all bet recommendations.

### **user-api/**
Serves predictions and explanations to your main app via REST API endpoints.

## Data Exchange

### Input (from your app):
```json
{
  "matches": [{
    "match_id": "12345",
    "datetime": "2025-11-15T14:00:00Z",
    "home_team": "Team A",
    "away_team": "Team B",
    "stats": {
      "home_goals_avg": 1.4,
      "away_goals_avg": 1.1,
      "home_corners_avg": 5.2,
      "away_corners_avg": 4.8
    },
    "odds": {
      "market_1": {
        "selection_1": 1.95,
        "selection_2": 3.5
      }
    }
  }]
}
```

### Output (to your app):
```json
{
  "predictions": [{
    "match_id": "12345",
    "smart_bets": [{
      "market_id": "market_1",
      "selection_id": "selection_1",
      "probability": 0.58
    }],
    "golden_bets": [{
      "market_id": "market_1",
      "selection_id": "selection_1",
      "confidence": 0.95
    }],
    "value_bets": [{
      "market_id": "market_1",
      "selection_id": "selection_1",
      "value": 0.12,
      "explanation": "Strong recent home form and high AI probability vs odds"
    }]
  }]
}
```

See [SCOPE.md](SCOPE.md) for complete data format specifications.

## Development Workflow

1. **Data Ingestion:**
   Build the data-ingestion module to receive and validate data from your app.

2. **Model Development:**
   Develop smart-bets-ai and golden-bets-ai models using XGBoost/LightGBM. Train on historical data.

3. **Odds Processing:**
   Create odds-updater to handle real-time odds updates from your app.

4. **Value Calculation:**
   Implement value-bets-ai to dynamically calculate value (AI prob - implied prob).

5. **Explanations & Serving:**
   Generate explanations through summary-generator and serve via user-api.

6. **Integration & Testing:**
   Connect modules via shared DBs, implement caching, validate with tests.

## AI Model Approach

### Baseline: XGBoost/LightGBM
- Probabilistic classification trained on historical match outcomes
- Outputs probability distributions for each bet market

### Smart Bets
Pure AI probabilities without considering odds

### Golden Bets
High confidence threshold (e.g., 0.90+) or ensemble agreement

### Value Bets
`Value = AI_Probability - Implied_Probability`  
Recalculated dynamically as odds change

### Future Enhancement
Neural networks or transformer models for deeper pattern recognition

## Tools & Technologies

- **Python** (AI models and APIs)
- **XGBoost / LightGBM** (baseline models)
- **FastAPI** (API endpoints)
- **PostgreSQL** (data storage)
- **Redis** (caching layer)
- **Docker** (containerization)
- **GitHub Actions** (CI/CD)

## Deployment & Scaling

- Cloud hosting (AWS, GCP, Azure)
- Docker Compose or Kubernetes
- Horizontal scaling for API endpoints
- Redis caching for sub-second response times
- Monitoring via logs, metrics, alerts

## System Flow

```
Your App → [JSON Input] → AI Prediction Engine → [JSON Output] → Your App
                              ↓
                    ┌─────────┴─────────┐
                    │                   │
              Smart Bets AI      Golden Bets AI
                    │                   │
                    └─────────┬─────────┘
                              ↓
                        Value Bets AI
                              ↓
                    Summary Generator
                              ↓
                         User API
                              ↓
                      [Cached Results]
```

## Notes

- System processes batch predictions each morning
- Odds updates trigger value bet recalculations
- All predictions cached for fast API responses
- Extensible to other sports by adding new models
- Focus on accuracy, explainability, and speed

---

**Ready to build the AI brain for your betting platform.**
