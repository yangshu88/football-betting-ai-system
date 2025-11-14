# Football Betting AI System

> **🎉 Phase 2 Complete!** Smart Bets AI is now fully functional. Train models and start making predictions!  
> **📊 Progress:** 50% Complete (2 of 5 phases done)  
> **✅ Working:** Data Ingestion, Smart Bets AI  
> **🔄 Next:** Golden Bets AI (85%+ confidence filtering)  
> **📖 Quick Start:** See [SMART_BETS_QUICKSTART.md](SMART_BETS_QUICKSTART.md)

---

## Overview
This project is the **AI prediction engine** - the intelligent core that analyzes football fixtures and generates betting predictions across **4 specific betting markets**. It receives data from your main app, runs AI models, and returns four distinct types of betting intelligence with transparent reasoning.

**This system is NOT the full betting app** - it's the AI brain that powers predictions. Your main app handles the frontend, data ingestion, user management, and payments.

## Target Markets (ONLY THESE 4)

This system focuses exclusively on:

1. **Goals: Over/Under 2.5**
2. **Cards: Over/Under 3.5** 
3. **Corners: Over/Under 9.5**
4. **BTTS (Both Teams To Score): Yes/No**

**Note:** We do NOT predict match results (home win/draw/away win), first/second half markets, or any other markets.

---

## What This System Does

✅ **Accepts data** from your app (fixtures, stats, odds for the 4 markets)  
✅ **Runs AI models** to generate predictions for the 4 markets  
✅ **Delivers four betting intelligence features:**
- **Golden Bets:** 1-3 daily picks with 85%+ win probability (safety-focused) *[Coming in Phase 3]*
- **Value Bets:** Top 3 daily picks with positive expected value (profit-focused) *[Coming in Phase 4]*
- **Smart Bets:** Best single bet per fixture across the 4 markets (match-specific) **[✅ WORKING NOW]**
- **Custom Bet Analysis:** User-selected fixture + bet type analysis from the 4 markets (interactive learning) *[Coming in Phase 5]*

✅ **Generates transparent explanations** for every recommendation  
✅ **Exposes API endpoints** for your app to query  
✅ **Caches predictions** for fast response times

## What This System Does NOT Do

❌ Frontend application  
❌ Data scraping from external sources  
❌ User authentication  
❌ Payment processing  
❌ Match result predictions (home/draw/away)  
❌ First/second half markets  
❌ Any markets outside the 4 specified

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Clone and install
git clone https://github.com/dannythehat/football-betting-ai-system.git
cd football-betting-ai-system
pip install -r requirements.txt

# 2. Train models
python smart-bets-ai/train.py

# 3. Test predictions
python smart-bets-ai/predict.py

# 4. Start API
cd user-api && python main.py

# 5. Make prediction
curl -X POST http://localhost:8000/api/v1/predictions/smart-bets \
  -H "Content-Type: application/json" \
  -d '{"matches": [...]}'
```

**Full guide:** [SMART_BETS_QUICKSTART.md](SMART_BETS_QUICKSTART.md)

---

## The Four Betting Intelligence Features

### 1. Golden Bets (Premium Feature) *[Phase 3 - Coming Soon]*
**Daily 1-3 picks | 85%+ win probability**

**Purpose:** Present users with the platform's most confident, safe betting opportunities each day from the 4 markets.

**Focus:** High win rate and consistency, regardless of bookmaker odds.

**Target Users:** Premium subscribers seeking top-tier, high-certainty bets with transparent AI reasoning.

**Value:** Builds credibility through consistently high-probability recommendations without overwhelming users.

**AI Approach:** 
- Confidence threshold filtering (85%+ probability)
- Ensemble model agreement metrics
- Historical validation of prediction accuracy
- Evaluates all 4 markets to find highest confidence picks

---

### 2. Value Bets (Premium Feature) *[Phase 4 - Coming Soon]*
**Daily top 3 picks | Positive expected value**

**Purpose:** Identify bets where potential return exceeds risk implied by the market across the 4 markets.

**Focus:** Long-term profitability through positive expected value (EV).

**Target Users:** Strategic bettors interested in maximizing ROI by focusing on market inefficiencies.

**Value:** Educates users on betting strategy beyond probability—focusing on value, which is key to successful sports betting.

**AI Approach:**
- `Value = AI_Probability - Implied_Probability`
- Dynamic recalculation as odds change
- Detailed explanations of why each bet offers value
- May have lower win rates than Golden Bets but higher long-term ROI
- Scans all 4 markets for value opportunities

---

### 3. Smart Bets (Per Fixture) **[✅ WORKING NOW]**
**Best single bet per match | All 4 markets analyzed**

**Purpose:** Provide tailored, detailed betting insight on individual matches.

**Focus:** Match-specific optimization across the 4 tracked markets.

**Target Users:** Users wanting in-depth, data-backed guidance for specific games they're interested in.

**Value:** Supports informed betting decisions with clear probability insights for specific fixtures.

**AI Approach:**
- Evaluates all 4 markets for each game
- Returns highest probability option with reasoning summary
- Pure probabilistic analysis without odds consideration
- Shows alternative markets with their probabilities

**Status:** ✅ Fully implemented and working  
**Documentation:** [smart-bets-ai/README.md](smart-bets-ai/README.md)  
**API Endpoint:** `POST /api/v1/predictions/smart-bets`

---

### 4. Custom Bet Analysis (Interactive Feature) *[Phase 5 - Coming Soon]*
**User-selected fixture + bet type | On-demand analysis**

**Purpose:** Empower users to test their own betting hypotheses independently.

**Focus:** Flexibility, transparency, and user education.

**Target Users:** Advanced or experimental users wanting control and personalized AI feedback.

**Value:** Allows interactive engagement with AI to deepen understanding of betting dynamics.

**AI Approach:**
- User selects any upcoming fixture and one of the 4 bet markets
- AI runs focused analysis on that specific bet
- Returns verdict (good/bad), probability estimates, and reasoning
- **Note:** Typically yields lower confidence than Smart Bets (which analyze all 4 markets), unless user's choice aligns with AI's top prediction

---

## Architecture
The system is composed of several interconnected modules:

### **data-ingestion/** ✅ Complete
Receives and validates fixture data, team stats, and odds for the 4 markets from your main app.

### **smart-bets-ai/** ✅ Complete
Calculates pure probabilistic predictions for each match across the 4 markets using AI models (XGBoost/LightGBM baseline).

### **golden-bets-ai/** 🔄 Next
Identifies high-confidence bets (85%+) across the 4 markets using confidence thresholds and ensemble agreement metrics.

### **odds-updater/** ⏳ Pending
Processes odds updates from your app for real-time value calculations across the 4 markets.

### **value-bets-ai/** ⏳ Pending
Dynamically recalculates value bets by comparing AI probabilities vs implied odds probabilities for the 4 markets.

### **summary-generator/** ⏳ Pending
Creates human-readable AI explanations for all bet recommendations with educational focus.

### **user-api/** ✅ Complete
Serves predictions and explanations to your main app via REST API endpoints.

---

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
      "home_goals_conceded_avg": 0.8,
      "away_goals_conceded_avg": 1.6,
      "home_corners_avg": 5.2,
      "away_corners_avg": 4.8,
      "home_cards_avg": 2.1,
      "away_cards_avg": 1.8,
      "home_btts_rate": 0.6,
      "away_btts_rate": 0.5
    },
    "odds": {
      "total_goals": {
        "over_2.5": 2.10,
        "under_2.5": 1.75
      },
      "total_cards": {
        "over_3.5": 1.95,
        "under_3.5": 1.85
      },
      "total_corners": {
        "over_9.5": 1.90,
        "under_9.5": 1.90
      },
      "btts": {
        "yes": 1.85,
        "no": 2.00
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
    "golden_bets": [{ }],
    "value_bets": [{ }],
    "smart_bets": [{
      "market_id": "total_corners",
      "market_name": "Total Corners",
      "selection_id": "over_9.5",
      "selection_name": "Over 9.5 Corners",
      "probability": 0.87,
      "explanation": "Highest probability outcome across all 4 analyzed markets for this fixture",
      "alternative_markets": [
        {
          "market_name": "BTTS Yes",
          "probability": 0.68
        },
        {
          "market_name": "Total Goals Over 2.5",
          "probability": 0.67
        },
        {
          "market_name": "Total Cards Over 3.5",
          "probability": 0.58
        }
      ]
    }]
  }]
}
```

See [SCOPE.md](SCOPE.md) for complete data format specifications.

---

## Development Workflow

1. **✅ Data Ingestion:** (Phase 1 - Complete)
   Build the data-ingestion module to receive and validate data from your app for the 4 markets.

2. **✅ Smart Bets AI:** (Phase 2 - Complete)
   Develop 4 separate models (Goals, Cards, Corners, BTTS) using XGBoost. Train on historical data.

3. **🔄 Golden Bets AI:** (Phase 3 - Next)
   Implement 85%+ confidence filtering and ensemble validation.

4. **⏳ Odds Processing & Value Bets:** (Phase 4 - Pending)
   Create odds-updater and value-bets-ai for dynamic EV calculations.

5. **⏳ Explanations & Polish:** (Phase 5 - Pending)
   Generate enhanced explanations, custom analysis, caching, and testing.

---

## AI Model Approach

### Market-Specific Models

The system trains **4 separate models**, one for each market:

1. **Goals Model:** Predicts Over/Under 2.5 goals
2. **Cards Model:** Predicts Over/Under 3.5 cards
3. **Corners Model:** Predicts Over/Under 9.5 corners
4. **BTTS Model:** Predicts Both Teams To Score Yes/No

### Baseline: XGBoost
- Probabilistic classification trained on historical match outcomes
- Outputs probability distributions for each of the 4 markets
- Focus on accuracy, explainability, and transparency
- Each model optimized for its specific market

### Golden Bets
- High confidence threshold (85%+)
- Ensemble agreement validation
- Historical win rate verification
- Scans all 4 markets for highest confidence picks

### Value Bets
`Value = AI_Probability - Implied_Probability`  
Recalculated dynamically as odds change across the 4 markets

### Smart Bets
Pure AI probabilities without considering odds, selecting highest probability across the 4 markets per fixture

### Custom Analysis
Same trained models applied to user-selected bets from the 4 markets with educational explanations

---

## Strategic Feature Positioning

| Feature | Focus | Confidence | Markets Analyzed | User Type |
|---------|-------|------------|------------------|-----------|\
| Golden Bets | Win rate | Highest (85%+) | All 4 markets | Premium - Safety seekers |\
| Value Bets | ROI/EV | Variable | All 4 markets | Premium - Strategic bettors |\
| Smart Bets | Per-match | High | All 4 markets | All users - Match focus |\
| Custom Analysis | Education | Variable | User-selected from 4 | Advanced - Learning |

**User Journey:**
1. Free users see Smart Bets (quality hook)
2. Premium users unlock Golden + Value Bets (curated daily picks)
3. Engaged users explore Custom Analysis (interactive learning)

---

## Tools & Technologies

- **Python** (AI models and APIs)
- **XGBoost** (baseline models for each market)
- **FastAPI** (API endpoints)
- **PostgreSQL** (data storage)
- **Redis** (caching layer)
- **Docker** (containerization)

---

## System Flow

```
Your App → [JSON Input] → AI Prediction Engine → [JSON Output] → Your App
                              ↓
                    ┌─────────┴─────────┐
                    │                   │
              Smart Bets AI      Golden Bets AI (85%+ threshold)
           (4 Market Models)      (4 Market Models)
                    │                   │
                    └─────────┬─────────┘
                              ↓
                        Value Bets AI (EV calculation)
                              ↓
                    Summary Generator (Transparent explanations)
                              ↓
                         User API
                              ↓
                      [Cached Results]
```

---

## Documentation

- **[STATUS.md](STATUS.md)** - Current project status and progress
- **[ROADMAP.md](ROADMAP.md)** - Implementation plan and timeline
- **[SCOPE.md](SCOPE.md)** - Technical specifications
- **[FEATURES.md](FEATURES.md)** - Detailed feature descriptions
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Setup instructions
- **[QUICKSTART.md](QUICKSTART.md)** - Developer quick start
- **[SMART_BETS_QUICKSTART.md](SMART_BETS_QUICKSTART.md)** - Smart Bets 5-minute guide
- **[PHASE_2_SUMMARY.md](PHASE_2_SUMMARY.md)** - Phase 2 implementation details
- **[smart-bets-ai/README.md](smart-bets-ai/README.md)** - Smart Bets AI documentation

---

## Notes

- System processes batch predictions each morning for the 4 markets
- Odds updates trigger value bet recalculations
- All predictions cached for fast API responses
- Custom analysis provides educational feedback with confidence context
- Focus on accuracy, explainability, transparency, and user education
- Laser-focused on 4 specific markets for high-quality predictions

**Ready to build the complete AI brain for your betting intelligence platform across Goals O/U 2.5, Cards O/U 3.5, Corners O/U 9.5, and BTTS Y/N.**
