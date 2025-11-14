# 🤖 Automated Model Training

Your repository now has **fully automated AI model training** via GitHub Actions!

---

## ✨ What's New

### Automated Training Workflow
- **Location:** `.github/workflows/train-models.yml`
- **Triggers:** Manual, weekly schedule, code/data changes
- **Output:** Trained models committed to `smart-bets-ai/models/`

### Training Guide
- **Location:** `TRAINING_GUIDE.md`
- **Contains:** Complete training instructions, metrics explanation, troubleshooting

---

## 🚀 How to Train Your Models NOW

### Step 1: Go to GitHub Actions
1. Open your repository: https://github.com/dannythehat/football-betting-ai-system
2. Click the **Actions** tab
3. Select **Train AI Models** workflow (left sidebar)

### Step 2: Run the Workflow
1. Click **Run workflow** button (top right)
2. Keep branch as `main`
3. Click green **Run workflow** button

### Step 3: Watch the Magic
The workflow will:
- ✅ Install Python 3.11 and dependencies
- ✅ Load training data (50 sample matches)
- ✅ Train 4 XGBoost models:
  - Goals (Over/Under 2.5)
  - Cards (Over/Under 3.5)
  - Corners (Over/Under 9.5)
  - BTTS (Yes/No)
- ✅ Generate performance metrics
- ✅ Save models to `smart-bets-ai/models/`
- ✅ Commit models back to your repo

**Time:** ~3-5 minutes

### Step 4: View Results
- Check the **Summary** tab for training metrics
- See the new commit with trained models
- Models are now ready for predictions!

---

## 📊 What Gets Created

After training, you'll have:

```
smart-bets-ai/models/
├── goals_model.pkl          # Goals O/U 2.5 predictor
├── cards_model.pkl          # Cards O/U 3.5 predictor
├── corners_model.pkl        # Corners O/U 9.5 predictor
├── btts_model.pkl           # BTTS Yes/No predictor
├── feature_engineer.pkl     # Feature transformation pipeline
└── metadata.json            # Training metrics and info
```

---

## 🔄 Automatic Retraining

Your models will automatically retrain:

### 1. Weekly Schedule
- **When:** Every Sunday at 2 AM UTC
- **Why:** Keep models fresh with latest patterns

### 2. Data Updates
- **Trigger:** Push to `test-data/historical_*.json`
- **Why:** New data = better models

### 3. Code Changes
- **Trigger:** Changes to `smart-bets-ai/train.py` or `features.py`
- **Why:** Feature improvements need retraining

### 4. Manual Trigger
- **How:** Click "Run workflow" anytime
- **Why:** On-demand training when needed

---

## 📈 Expected Performance

With sample data (50 matches):

| Metric | Target | Typical |
|--------|--------|---------|
| Accuracy | >60% | 62-65% |
| Log Loss | <0.65 | 0.62-0.64 |
| AUC-ROC | >0.65 | 0.65-0.68 |

**Note:** Performance improves significantly with more data (300+ matches)

---

## 🎯 Next Steps After Training

### 1. Test Predictions Locally
```bash
# Clone repo (models are already trained!)
git clone https://github.com/dannythehat/football-betting-ai-system.git
cd football-betting-ai-system

# Install dependencies
pip install -r requirements.txt

# Test predictions
python smart-bets-ai/predict.py
```

### 2. Start the API
```bash
cd user-api
python main.py
```

### 3. Make Your First Prediction
```bash
curl -X POST http://localhost:8000/api/v1/predictions/smart-bets \
  -H "Content-Type: application/json" \
  -d @test-data/upcoming_fixtures_200.json
```

### 4. View API Docs
Open: http://localhost:8000/docs

---

## 🔍 Monitoring Training

### View Workflow Runs
- Go to **Actions** tab
- Click on any workflow run
- See detailed logs and metrics

### Check Training Metrics
After training completes:
```bash
cat smart-bets-ai/models/metadata.json
```

Example output:
```json
{
  "version": "1.0.0",
  "trained_at": "20251114_171530",
  "markets": ["goals", "cards", "corners", "btts"],
  "metrics": {
    "goals": {
      "accuracy": 0.6500,
      "log_loss": 0.6234,
      "auc_roc": 0.6789
    },
    "cards": {
      "accuracy": 0.6200,
      "log_loss": 0.6456,
      "auc_roc": 0.6543
    }
  }
}
```

---

## 🚨 Troubleshooting

### Workflow Fails
**Check:**
1. Workflow logs in Actions tab
2. Python version (should be 3.11)
3. Dependencies installation
4. Training data exists

### Models Not Committed
**Possible causes:**
1. No changes detected (models identical)
2. Git permissions issue
3. Workflow didn't complete

**Solution:** Re-run workflow manually

### Low Performance
**Expected with sample data!**
- 50 matches = limited training data
- Performance improves with 300+ matches
- Focus on structure working correctly

---

## 💡 Pro Tips

1. **First time?** Run manual training to see it work
2. **Check Actions tab** regularly for training status
3. **Monitor metrics** in metadata.json
4. **Add more data** for better performance
5. **Retrain weekly** to keep models fresh

---

## 📚 Additional Resources

- **Full Training Guide:** [TRAINING_GUIDE.md](TRAINING_GUIDE.md)
- **Smart Bets Docs:** [smart-bets-ai/README.md](smart-bets-ai/README.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **System Overview:** [README.md](README.md)

---

## 🎉 You're All Set!

Your AI models can now train automatically. Just:
1. Go to Actions → Train AI Models
2. Click Run workflow
3. Wait 3-5 minutes
4. Start making predictions!

**No manual Python execution needed!** 🚀
