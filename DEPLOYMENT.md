# 🚀 Deployment Guide

## Automated System Status

✅ **Fully Automated** - Models train and test automatically every 6 hours
✅ **GitHub Actions** - All testing runs in CI/CD pipeline
✅ **No Manual Intervention** - System self-maintains

## Current Deployment: Render

**Platform:** Render (Free Tier)
**Status:** Ready to deploy
**Auto-deploy:** Enabled from main branch

### Why Render?
- ✅ Free tier with 750 hours/month
- ✅ Auto-deploy from GitHub
- ✅ Built-in PostgreSQL + Redis (free)
- ✅ Zero configuration needed
- ✅ Actually reliable (unlike Railway)

---

## 🚀 Deploy to Render (5 Minutes)

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub
3. Authorize Render to access your repos

### Step 2: Deploy from Dashboard
1. Click **"New +"** → **"Blueprint"**
2. Connect your GitHub repo: `dannythehat/football-betting-ai-system`
3. Render will detect `render.yaml` automatically
4. Click **"Apply"**
5. Wait 3-5 minutes for deployment

### Step 3: Verify Deployment
```bash
# Check health endpoint (replace with your Render URL)
curl https://football-betting-ai.onrender.com/health

# Expected response:
{
  "status": "healthy",
  "service": "football-betting-ai",
  "version": "1.0.0",
  "smart_bets_available": true,
  "golden_bets_available": true,
  "value_bets_available": true,
  "custom_analysis_available": true
}
```

**That's it! Your API is live.**

---

## 📋 What Gets Deployed

The `render.yaml` file automatically creates:

1. **Web Service** (Free tier)
   - FastAPI application
   - Auto-deploy on push to main
   - Health checks enabled
   - 750 hours/month free

2. **PostgreSQL Database** (Free tier)
   - 256MB storage
   - Automatic backups
   - Connection string auto-configured

3. **Redis Cache** (Free tier)
   - 25MB storage
   - LRU eviction policy
   - Connection string auto-configured

---

## 🔧 Configuration

### Environment Variables (Auto-configured)
All environment variables are set automatically by `render.yaml`:
- `DATABASE_URL` - PostgreSQL connection
- `REDIS_URL` - Redis connection
- `PYTHON_VERSION` - 3.11.0
- `ENVIRONMENT` - production
- `DEBUG` - false

### Custom Environment Variables
To add custom variables:
1. Go to Render Dashboard
2. Select your service
3. Go to **Environment** tab
4. Add variables
5. Service auto-restarts

---

## 🤖 What's Automated

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
- **Platform:** Render
- **Trigger:** Auto-deploy on push to main
- **Services:**
  - FastAPI application
  - PostgreSQL database
  - Redis cache

---

## 📡 API Endpoints

Base URL: `https://your-app-name.onrender.com`

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
  "match_data": {...},
  "market_id": "goals_over_2_5",
  "selection_id": "over"
}
```

---

## 🔍 Monitoring

### Render Dashboard
- View logs: Dashboard → Service → Logs
- Check metrics: Dashboard → Service → Metrics
- View deployments: Dashboard → Service → Events

### GitHub Actions
All workflows visible at:
https://github.com/dannythehat/football-betting-ai-system/actions

### Test Results
Check `test-results/TEST_REPORT.md` in repo

### Model Metrics
Check `smart-bets-ai/models/metadata.json`

---

## 🐛 Troubleshooting

### Deployment Failed?
1. Check Render logs in dashboard
2. Verify `render.yaml` syntax
3. Check if all dependencies in `requirements.txt`
4. Ensure Python 3.11 compatibility

### Models Not Loading?
1. Check if models exist in `smart-bets-ai/models/`
2. Run training workflow manually
3. Check GitHub Actions logs
4. Verify model files committed to repo

### Database Connection Issues?
1. Verify PostgreSQL service is running in Render
2. Check `DATABASE_URL` environment variable
3. Review connection logs
4. Ensure database migrations ran

### API Not Responding?
1. Check health endpoint first
2. Review Render service logs
3. Verify service is not sleeping (free tier sleeps after 15min inactivity)
4. Check if deployment completed successfully

---

## 💡 Free Tier Limitations

### Render Free Tier
- **Web Service:** 750 hours/month (enough for testing)
- **Sleeps after 15 minutes** of inactivity
- **Cold start:** 30-60 seconds on first request after sleep
- **PostgreSQL:** 256MB storage
- **Redis:** 25MB storage

### Upgrade Options
- **Starter Plan:** $7/month - No sleep, always on
- **Standard Plan:** $25/month - More resources, faster
- **Pro Plan:** $85/month - Production-grade

---

## 🚀 Alternative Deployment Options

### Option 1: DigitalOcean App Platform
```bash
# More reliable, $5/month
# Better for production
# Managed database available
```

### Option 2: Self-Hosted VPS
```bash
# Full control, $5/month
# DigitalOcean, Linode, Hetzner
# Requires more setup
```

### Option 3: AWS Lambda
```bash
# Serverless, pay per request
# Infinite scale
# More complex setup
```

---

## 📚 Next Steps

1. ✅ Deploy to Render (5 minutes)
2. ✅ Verify health endpoint works
3. ✅ Test API endpoints
4. ✅ Monitor GitHub Actions workflows
5. ✅ Check test results in repo
6. 🎯 Start building features!

---

## ✅ Current Status: READY TO DEPLOY

**All systems automated and working:**
- ✅ Models training automatically
- ✅ Tests running every 6 hours
- ✅ Deployment configuration ready
- ✅ API endpoints functional
- ✅ Documentation complete
- ✅ No manual intervention required

**Deploy now:** https://render.com

**System is production-ready and self-maintaining.**
