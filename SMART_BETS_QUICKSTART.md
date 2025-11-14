# Smart Bets AI - Quick Start Guide

## 🚀 Get Smart Bets Running in 5 Minutes

This guide will get you from zero to making Smart Bets predictions.

---

## Prerequisites

- Python 3.9+
- pip
- Git

---

## Step 1: Clone & Setup (1 minute)

```bash
# Clone repository
git clone https://github.com/dannythehat/football-betting-ai-system.git
cd football-betting-ai-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Step 2: Train Models (2 minutes)

```bash
# Train Smart Bets AI models
python smart-bets-ai/train.py
```

**Expected Output:**
```
============================================================
SMART BETS AI - MODEL TRAINING
============================================================
✅ Loaded 50 matches from test-data/historical_matches_sample.json

🔄 Training GOALS model...
✅ GOALS Model Performance:
   Accuracy: 0.7000
   Log Loss: 0.5234
   AUC-ROC: 0.7500

🔄 Training CARDS model...
✅ CARDS Model Performance:
   Accuracy: 0.6500
   Log Loss: 0.6123
   AUC-ROC: 0.6800

🔄 Training CORNERS model...
✅ CORNERS Model Performance:
   Accuracy: 0.7200
   Log Loss: 0.5012
   AUC-ROC: 0.7800

🔄 Training BTTS model...
✅ BTTS Model Performance:
   Accuracy: 0.6800
   Log Loss: 0.5678
   AUC-ROC: 0.7200

💾 Saved goals model to smart-bets-ai/models/goals_model.pkl
💾 Saved cards model to smart-bets-ai/models/cards_model.pkl
💾 Saved corners model to smart-bets-ai/models/corners_model.pkl
💾 Saved btts model to smart-bets-ai/models/btts_model.pkl
💾 Saved feature engineer to smart-bets-ai/models/feature_engineer.pkl
💾 Saved metadata to smart-bets-ai/models/metadata.json

============================================================
✅ TRAINING COMPLETE
============================================================
```

---

## Step 3: Test Predictions (30 seconds)

```bash
# Test prediction service
python smart-bets-ai/predict.py
```

**Expected Output:**
```
============================================================
SMART BETS PREDICTION TEST
============================================================
✅ Loaded 4 models

✅ Smart Bet for Manchester United vs Liverpool:
   Market: Over 9.5 Corners
   Probability: 87.3%
   Explanation: Highest probability outcome across all 4 analyzed markets...

   Alternative Markets:
   - Yes: 68.5%
   - Over 2.5 Goals: 67.2%
   - Over 3.5 Cards: 58.1%
```

---

## Step 4: Start API Server (30 seconds)

```bash
# Start FastAPI server
cd user-api
python main.py
```

**Expected Output:**
```
✅ Database initialized successfully
✅ Smart Bets AI models loaded
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## Step 5: Make Your First Prediction (1 minute)

### Option A: Using curl

```bash
curl -X POST http://localhost:8000/api/v1/predictions/smart-bets \
  -H "Content-Type: application/json" \
  -d '{
    "matches": [{
      "match_id": "TEST_001",
      "home_team": "Manchester City",
      "away_team": "Arsenal",
      "home_goals_avg": 2.3,
      "away_goals_avg": 1.9,
      "home_goals_conceded_avg": 0.7,
      "away_goals_conceded_avg": 1.1,
      "home_corners_avg": 7.5,
      "away_corners_avg": 6.2,
      "home_cards_avg": 1.8,
      "away_cards_avg": 2.3,
      "home_btts_rate": 0.72,
      "away_btts_rate": 0.68,
      "home_form": "WWWWW",
      "away_form": "WWDWL"
    }]
  }'
```

### Option B: Using Python

```python
import requests

response = requests.post(
    'http://localhost:8000/api/v1/predictions/smart-bets',
    json={
        'matches': [{
            'match_id': 'TEST_001',
            'home_team': 'Manchester City',
            'away_team': 'Arsenal',
            'home_goals_avg': 2.3,
            'away_goals_avg': 1.9,
            'home_goals_conceded_avg': 0.7,
            'away_goals_conceded_avg': 1.1,
            'home_corners_avg': 7.5,
            'away_corners_avg': 6.2,
            'home_cards_avg': 1.8,
            'away_cards_avg': 2.3,
            'home_btts_rate': 0.72,
            'away_btts_rate': 0.68,
            'home_form': 'WWWWW',
            'away_form': 'WWDWL'
        }]
    }
)

print(response.json())
```

### Option C: Using API Docs

1. Open browser: http://localhost:8000/docs
2. Find `POST /api/v1/predictions/smart-bets`
3. Click "Try it out"
4. Paste the JSON request
5. Click "Execute"

---

## Expected Response

```json
{
  "success": true,
  "total_matches": 1,
  "predictions": [
    {
      "match_id": "TEST_001",
      "smart_bet": {
        "market_id": "btts",
        "market_name": "Both Teams To Score",
        "selection_id": "yes",
        "selection_name": "Yes",
        "probability": 0.8234,
        "percentage": "82.3%",
        "explanation": "Highest probability outcome across all 4 analyzed markets for this fixture. Both teams have strong scoring records with combined BTTS rate of 70.0%.",
        "alternative_markets": [
          {
            "market_name": "Over 2.5 Goals",
            "probability": 0.7891
          },
          {
            "market_name": "Over 9.5 Corners",
            "probability": 0.7456
          },
          {
            "market_name": "Over 3.5 Cards",
            "probability": 0.5123
          }
        ]
      }
    }
  ],
  "model_version": "1.0.0"
}
```

---

## 🎉 Success!

You now have Smart Bets AI running and making predictions!

---

## What Just Happened?

1. **Trained 4 Models:** One for each market (Goals, Cards, Corners, BTTS)
2. **Feature Engineering:** Transformed raw stats into ML features
3. **Smart Bet Selection:** AI analyzed all 4 markets and picked the highest probability
4. **API Integration:** Served predictions via REST API

---

## Next Steps

### Improve Model Accuracy
```bash
# Generate more training data
cd test-data
python generate_test_data.py --matches 1000

# Retrain with more data
python smart-bets-ai/train.py
```

### Integrate with Your App
```python
# Your main app sends match data
import requests

matches = get_upcoming_matches()  # Your function
response = requests.post(
    'http://your-ai-server:8000/api/v1/predictions/smart-bets',
    json={'matches': matches}
)

smart_bets = response.json()['predictions']
display_to_users(smart_bets)  # Your function
```

### Build Golden Bets (Phase 3)
- Filter predictions with 85%+ confidence
- Implement ensemble validation
- Create Golden Bets endpoint

---

## Troubleshooting

### Models Not Loading
```bash
# Check if models exist
ls smart-bets-ai/models/

# If empty, train models
python smart-bets-ai/train.py
```

### Import Errors
```bash
# Ensure you're in project root
pwd  # Should show: .../football-betting-ai-system

# Reinstall dependencies
pip install -r requirements.txt
```

### Low Accuracy
- Current models trained on 50 sample matches
- Production needs 1000+ historical matches
- Generate more data: `python test-data/generate_test_data.py`

### API Not Starting
```bash
# Check port availability
lsof -i :8000  # On Linux/Mac
netstat -ano | findstr :8000  # On Windows

# Use different port
export API_PORT=8001
python user-api/main.py
```

---

## Resources

- **Full Documentation:** `README.md`
- **Smart Bets Details:** `smart-bets-ai/README.md`
- **API Docs:** http://localhost:8000/docs (when server running)
- **Project Status:** `STATUS.md`
- **Roadmap:** `ROADMAP.md`

---

## Support

Having issues? Check:
1. Python version: `python --version` (need 3.9+)
2. Dependencies installed: `pip list`
3. Models trained: `ls smart-bets-ai/models/`
4. Server running: `curl http://localhost:8000/health`

---

**🎯 You're now ready to generate Smart Bets predictions!**
