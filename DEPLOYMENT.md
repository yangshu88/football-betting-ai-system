# 🚀 Deployment Guide

## Automated System Status

✅ **Fully Automated** - Models train and test automatically every 6 hours
✅ **GitHub Actions** - All testing runs in CI/CD pipeline
✅ **No Manual Intervention** - System self-maintains

## Current Deployment: Railway

**Live URL:** https://football-betting-ai-system-production.up.railway.app
**Status:** ✅ Active
**Last Deploy:** Auto-deployed from main branch

## What's Automated

### 1. Model Training
- **Frequency:** Weekly (Sundays 2 AM UTC) + on-demand
- **Workflow:** `.github/workflows/train-models.yml`
- **Output:** Trained models committed to repo
- **Metrics:** Automatically logged in `smart-bets-ai/models/metadata.json`

### 2. Testing
- **Frequency:** Every 6 hours + on every push
- **Workflow:** `.github/workflows/full-test-deploy.yml`
- **Tests:**
  - Smart Bets AI predictions
  - Golden Bets filtering
  - Value Bets calculations
  - Custom Analysis engine
- **Results:** Saved to `test-results/TEST_REPORT.md`

### 3. Deployment
- **Platform:** Railway
- **Trigger:** Auto-deploy on push to main
- **Services:**
  - FastAPI application
  - PostgreSQL database
  - Redis cache

## Manual Deployment Options

### Option 1: Railway (Recommended)
```bash
# Already deployed! Just push to main branch
git push origin main
```

### Option 2: Render
```bash
# Connect GitHub repo to Render
# Set environment variables from .env.example
# Deploy automatically
```

### Option 3: Docker Compose (Local)
```bash
docker-compose up -d
```

## Environment Variables

Required for production:
```env
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379/0
API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=production
DEBUG=false
```

## API Endpoints

Base URL: `https://football-betting-ai-system-production.up.railway.app`

### Health Check
```bash
GET /health
```

### Smart Bets
```bash
POST /api/v1/predictions/smart-bets
Content-Type: application/json

{
  "matches": [...]
}
```

### Golden Bets
```bash
POST /api/v1/predictions/golden-bets
Content-Type: application/json

{
  "matches": [...]
}
```

### Value Bets
```bash
POST /api/v1/predictions/value-bets
Content-Type: application/json

{
  "matches": [...]
}
```

### Custom Analysis
```bash
POST /api/v1/predictions/custom-analysis
Content-Type: application/json

{
  "match": {...},
  "bet_type": "goals_over_2_5"
}
```

## Monitoring

### Check Workflow Status
https://github.com/dannythehat/football-betting-ai-system/actions

### View Test Results
Check `test-results/TEST_REPORT.md` in repo

### View Model Metrics
Check `smart-bets-ai/models/metadata.json`

## Troubleshooting

### Models not training?
- Check workflow runs: https://github.com/dannythehat/football-betting-ai-system/actions
- Manually trigger: Go to Actions → Train AI Models → Run workflow

### Tests failing?
- Check test results in `test-results/`
- Review workflow logs

### Deployment issues?
- Check Railway logs
- Verify environment variables
- Ensure database is accessible

## Next Steps

1. ✅ Models are training automatically
2. ✅ Tests run every 6 hours
3. ✅ Deployment is live on Railway
4. 📊 Monitor test results in repo
5. 🔄 System self-maintains

**No manual intervention required!**
