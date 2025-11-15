# 📡 API Documentation

## Base URL
```
Production: https://football-betting-ai-system-production.up.railway.app
Local: http://localhost:8000
```

## Authentication
Currently no authentication required. Add API keys in production.

## Endpoints

### Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-15T04:00:00Z",
  "version": "1.0.0"
}
```

---

### Smart Bets - Best Bet Per Match
```http
POST /api/v1/predictions/smart-bets
Content-Type: application/json
```

**Request Body:**
```json
{
  "matches": [
    {
      "id": "match_123",
      "home_team": "Manchester United",
      "away_team": "Liverpool",
      "date": "2025-11-20T15:00:00Z",
      "stats": {
        "home_goals_avg": 2.1,
        "away_goals_avg": 1.8,
        "home_cards_avg": 2.3,
        "away_cards_avg": 2.5,
        "home_corners_avg": 5.2,
        "away_corners_avg": 4.8
      },
      "odds": {
        "goals_over_2_5": 1.85,
        "goals_under_2_5": 2.10,
        "cards_over_3_5": 2.20,
        "cards_under_3_5": 1.75,
        "corners_over_9_5": 1.95,
        "corners_under_9_5": 1.90,
        "btts_yes": 1.70,
        "btts_no": 2.25
      }
    }
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "match_id": "match_123",
      "home_team": "Manchester United",
      "away_team": "Liverpool",
      "best_bet": {
        "market": "goals_over_2_5",
        "prediction": "over",
        "confidence": 0.873,
        "odds": 1.85,
        "reasoning": "Both teams averaging 2+ goals per game. High-scoring fixture expected."
      }
    }
  ],
  "timestamp": "2025-11-15T04:00:00Z"
}
```

---

### Golden Bets - Daily Premium Picks
```http
POST /api/v1/predictions/golden-bets
Content-Type: application/json
```

**Request Body:** Same as Smart Bets

**Response:**
```json
{
  "golden_bets": [
    {
      "match_id": "match_123",
      "home_team": "Manchester United",
      "away_team": "Liverpool",
      "market": "goals_over_2_5",
      "prediction": "over",
      "confidence": 0.892,
      "odds": 1.85,
      "reasoning": "Extremely high confidence based on recent form and head-to-head stats."
    },
    {
      "match_id": "match_456",
      "home_team": "Arsenal",
      "away_team": "Chelsea",
      "market": "btts_yes",
      "prediction": "yes",
      "confidence": 0.867,
      "odds": 1.70,
      "reasoning": "Both teams scoring consistently. Strong attacking records."
    }
  ],
  "count": 2,
  "min_confidence": 0.85,
  "timestamp": "2025-11-15T04:00:00Z"
}
```

---

### Value Bets - Positive Expected Value
```http
POST /api/v1/predictions/value-bets
Content-Type: application/json
```

**Request Body:** Same as Smart Bets

**Response:**
```json
{
  "value_bets": [
    {
      "match_id": "match_789",
      "home_team": "Barcelona",
      "away_team": "Real Madrid",
      "market": "corners_over_9_5",
      "prediction": "over",
      "confidence": 0.782,
      "odds": 2.10,
      "expected_value": 0.153,
      "ev_percentage": "+15.3%",
      "reasoning": "Odds significantly higher than true probability. Strong value opportunity."
    }
  ],
  "count": 3,
  "min_ev": 0.10,
  "timestamp": "2025-11-15T04:00:00Z"
}
```

---

### Custom Analysis - User-Selected Fixture
```http
POST /api/v1/predictions/custom-analysis
Content-Type: application/json
```

**Request Body:**
```json
{
  "match": {
    "id": "match_123",
    "home_team": "Manchester United",
    "away_team": "Liverpool",
    "date": "2025-11-20T15:00:00Z",
    "stats": {
      "home_goals_avg": 2.1,
      "away_goals_avg": 1.8,
      "home_cards_avg": 2.3,
      "away_cards_avg": 2.5,
      "home_corners_avg": 5.2,
      "away_corners_avg": 4.8
    },
    "odds": {
      "goals_over_2_5": 1.85,
      "cards_over_3_5": 2.20,
      "corners_over_9_5": 1.95,
      "btts_yes": 1.70
    }
  },
  "bet_type": "goals_over_2_5"
}
```

**Response:**
```json
{
  "analysis": {
    "match_id": "match_123",
    "home_team": "Manchester United",
    "away_team": "Liverpool",
    "bet_type": "goals_over_2_5",
    "prediction": "over",
    "confidence": 0.784,
    "odds": 1.85,
    "reasoning": "Detailed AI analysis of why this bet is recommended",
    "key_factors": [
      "Both teams averaging 2+ goals per game",
      "Recent head-to-head matches high-scoring",
      "Strong attacking form for both sides"
    ],
    "risk_assessment": "Medium risk - confidence above 75%",
    "educational_notes": "This market focuses on total goals scored by both teams combined."
  },
  "timestamp": "2025-11-15T04:00:00Z"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request format",
  "details": "Missing required field: matches"
}
```

### 500 Internal Server Error
```json
{
  "error": "Prediction failed",
  "details": "Model not loaded"
}
```

---

## Rate Limits
- **Development:** No limits
- **Production:** 100 requests/minute per IP

## Data Requirements

### Minimum Stats Required
- Goals average (home/away)
- Cards average (home/away)
- Corners average (home/away)

### Odds Required
All 8 odds for the 4 markets:
- goals_over_2_5 / goals_under_2_5
- cards_over_3_5 / cards_under_3_5
- corners_over_9_5 / corners_under_9_5
- btts_yes / btts_no

---

## Testing the API

### Using cURL
```bash
# Health check
curl https://football-betting-ai-system-production.up.railway.app/health

# Smart Bets
curl -X POST https://football-betting-ai-system-production.up.railway.app/api/v1/predictions/smart-bets \
  -H "Content-Type: application/json" \
  -d @sample-request.json
```

### Using Python
```python
import requests

url = "https://football-betting-ai-system-production.up.railway.app/api/v1/predictions/smart-bets"
data = {
    "matches": [...]
}

response = requests.post(url, json=data)
print(response.json())
```

### Using JavaScript
```javascript
const response = await fetch(
  'https://football-betting-ai-system-production.up.railway.app/api/v1/predictions/smart-bets',
  {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ matches: [...] })
  }
);

const data = await response.json();
console.log(data);
```

---

## Integration Guide

1. **Collect match data** from your data source
2. **Format request** according to schema above
3. **Send POST request** to appropriate endpoint
4. **Parse response** and display to users
5. **Cache results** for 30 minutes (optional)

---

## Support

For API issues:
- Check workflow logs: https://github.com/dannythehat/football-betting-ai-system/actions
- Review test results: `test-results/TEST_REPORT.md`
- Verify deployment: Railway dashboard
