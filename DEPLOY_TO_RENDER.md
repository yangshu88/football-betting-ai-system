# 🚀 Deploy to Render in 5 Minutes

## Why Render?
- ✅ **Free tier** - 750 hours/month (enough for testing)
- ✅ **Actually works** - Unlike Railway
- ✅ **Auto-deploy** - Push to main = instant deploy
- ✅ **Free database** - PostgreSQL + Redis included
- ✅ **Zero config** - `render.yaml` handles everything

---

## Step-by-Step Deployment

### 1. Create Render Account (1 minute)
1. Go to https://render.com
2. Click **"Get Started"**
3. Sign up with GitHub
4. Authorize Render to access your repositories

### 2. Deploy as Blueprint (2 minutes)
1. In Render Dashboard, click **"New +"**
2. Select **"Blueprint"**
3. Connect your repository: `dannythehat/football-betting-ai-system`
4. Render will detect `render.yaml` automatically
5. Click **"Apply"**

### 3. Wait for Deployment (2-3 minutes)
Render will automatically:
- Create web service (FastAPI app)
- Create PostgreSQL database (free tier)
- Create Redis cache (free tier)
- Install dependencies
- Start your API

You'll see progress in the dashboard.

### 4. Get Your API URL
Once deployed, you'll see:
```
https://football-betting-ai-XXXX.onrender.com
```

Copy this URL.

### 5. Test Your API (30 seconds)
```bash
# Replace with your actual URL
curl https://football-betting-ai-XXXX.onrender.com/health

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

**Done! Your API is live.**

---

## What Just Happened?

Render automatically created:

### 1. Web Service
- **Name:** football-betting-ai
- **Type:** Python web service
- **Plan:** Free (750 hours/month)
- **Auto-deploy:** Enabled on push to main
- **Health checks:** Enabled at `/health`

### 2. PostgreSQL Database
- **Name:** football-betting-db
- **Plan:** Free (256MB storage)
- **Connection:** Auto-configured via `DATABASE_URL`
- **Backups:** Automatic

### 3. Redis Cache
- **Name:** football-betting-redis
- **Plan:** Free (25MB storage)
- **Connection:** Auto-configured via `REDIS_URL`
- **Eviction:** LRU policy

---

## Free Tier Limitations

### What You Get (Free)
- ✅ 750 hours/month web service
- ✅ 256MB PostgreSQL database
- ✅ 25MB Redis cache
- ✅ Auto-deploy from GitHub
- ✅ SSL certificates
- ✅ Custom domains

### Limitations
- ⚠️ **Sleeps after 15 minutes** of inactivity
- ⚠️ **Cold start:** 30-60 seconds after sleep
- ⚠️ **Limited resources:** 512MB RAM

### When to Upgrade ($7/month)
- Need always-on service (no sleep)
- Higher traffic
- Faster performance
- Production use

---

## Using Your API

### Base URL
```
https://football-betting-ai-XXXX.onrender.com
```

### Endpoints

#### Health Check
```bash
GET /health
```

#### Smart Bets
```bash
POST /api/v1/predictions/smart-bets
Content-Type: application/json

{
  "matches": [
    {
      "match_id": "123",
      "home_team": "Arsenal",
      "away_team": "Chelsea",
      "home_goals_avg": 2.1,
      "away_goals_avg": 1.8,
      ...
    }
  ]
}
```

#### Golden Bets
```bash
POST /api/v1/predictions/golden-bets
Content-Type: application/json

{
  "matches": [...]
}
```

#### Value Bets
```bash
POST /api/v1/predictions/value-bets
Content-Type: application/json

{
  "matches": [
    {
      "match_id": "123",
      "home_team": "Arsenal",
      "away_team": "Chelsea",
      "odds": {
        "goals_over_2_5": 1.85,
        "btts_yes": 1.90
      },
      ...
    }
  ]
}
```

#### Custom Analysis
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

## Auto-Deploy Setup

### Already Configured!
Every push to `main` branch automatically deploys to Render.

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Render automatically:
# 1. Detects push
# 2. Pulls latest code
# 3. Installs dependencies
# 4. Restarts service
# 5. Your changes are live!
```

---

## Monitoring

### View Logs
1. Go to Render Dashboard
2. Click your service
3. Click **"Logs"** tab
4. See real-time logs

### View Metrics
1. Go to Render Dashboard
2. Click your service
3. Click **"Metrics"** tab
4. See CPU, memory, requests

### Check Deployments
1. Go to Render Dashboard
2. Click your service
3. Click **"Events"** tab
4. See deployment history

---

## Troubleshooting

### Service Not Starting?
1. Check logs in Render Dashboard
2. Verify `requirements.txt` has all dependencies
3. Check if models exist in repo
4. Ensure Python 3.11 compatibility

### Database Connection Failed?
1. Verify PostgreSQL service is running
2. Check `DATABASE_URL` in environment variables
3. Review connection logs
4. Ensure migrations ran

### API Returns 404?
1. Check if service is sleeping (free tier)
2. Wait 30-60 seconds for cold start
3. Verify deployment completed successfully
4. Check logs for errors

### Models Not Loading?
1. Ensure models are committed to repo
2. Check `smart-bets-ai/models/` directory
3. Run training workflow manually
4. Verify model files exist

---

## Next Steps

### 1. Test Your API
```bash
curl https://your-app-name.onrender.com/health
```

### 2. Update Your Code
```bash
git add .
git commit -m "New feature"
git push origin main
# Auto-deploys to Render!
```

### 3. Monitor Performance
- Check Render Dashboard regularly
- Review logs for errors
- Monitor response times

### 4. Upgrade When Ready
- $7/month for always-on
- No sleep, faster performance
- Better for production

---

## Support

### Render Documentation
https://render.com/docs

### This Project Documentation
- [DEPLOYMENT.md](DEPLOYMENT.md) - Full deployment guide
- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API reference
- [README.md](README.md) - Project overview

### Issues?
Open an issue on GitHub or check workflow logs.

---

## Summary

✅ **Deployed:** Your API is live on Render
✅ **Auto-deploy:** Push to main = instant deploy
✅ **Free tier:** 750 hours/month
✅ **Database:** PostgreSQL + Redis included
✅ **Monitoring:** Logs and metrics available

**Your API URL:** `https://your-app-name.onrender.com`

**Start using it now!**
