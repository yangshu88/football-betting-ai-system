# Test Data Documentation

## Overview
This directory contains realistic test data representing what your main app API will provide to the AI prediction engine.

## Data Structure

### 1. Historical Matches (Training Data)
**File:** `historical_matches.json`
- **Purpose:** Train AI models on past results
- **Time Range:** 3 years (2022-2025)
- **Records:** 600 matches (200 per year)
- **Contains:**
  - Match results (home goals, away goals, winner)
  - Team statistics at time of match
  - Actual odds from bookmakers
  - Outcomes for all betting markets

### 2. Upcoming Fixtures (Prediction Data)
**File:** `upcoming_fixtures.json`
- **Purpose:** Test prediction generation
- **Records:** 50 upcoming matches
- **Contains:**
  - Match details (teams, datetime)
  - Current team statistics
  - Current bookmaker odds
  - No results (to be predicted)

### 3. Team Statistics Database
**File:** `team_statistics.json`
- **Purpose:** Aggregated team performance data
- **Records:** 40 teams
- **Contains:**
  - Overall stats (goals, wins, losses)
  - Home/away splits
  - Form indicators
  - Historical trends

### 4. Database Schema
**File:** `schema.sql`
- PostgreSQL schema for storing all data
- Includes indexes for performance
- Foreign key relationships

## Betting Markets Covered

All test data includes odds and outcomes for:

1. **Match Result (1X2)**
   - Home Win
   - Draw
   - Away Win

2. **Total Goals (Over/Under)**
   - Over 0.5, 1.5, 2.5, 3.5, 4.5
   - Under 0.5, 1.5, 2.5, 3.5, 4.5

3. **Both Teams To Score (BTTS)**
   - Yes
   - No

4. **Double Chance**
   - Home or Draw
   - Away or Draw
   - Home or Away

5. **Corners**
   - Over/Under 8.5, 9.5, 10.5, 11.5
   - Home/Away corners

6. **Cards**
   - Over/Under 3.5, 4.5, 5.5 total cards

## Data Realism

### Team Distribution
- 40 teams across different skill levels
- 10 top-tier teams (strong home/away)
- 15 mid-tier teams (balanced)
- 15 lower-tier teams (inconsistent)

### Statistical Realism
- Goals: 0-6 range (realistic distribution)
- Corners: 4-14 range per team
- Cards: 1-7 range per match
- Form: Last 5 matches (W/D/L)
- Odds: Market-realistic ranges

### Historical Patterns
- Home advantage reflected (55% home win rate)
- Form impacts results
- Head-to-head history considered
- Seasonal variations included

## Usage

### For Model Training
```python
# Load historical data
with open('test-data/historical_matches.json') as f:
    training_data = json.load(f)

# Extract features and labels
# Train XGBoost/LightGBM models
```

### For Prediction Testing
```python
# Load upcoming fixtures
with open('test-data/upcoming_fixtures.json') as f:
    fixtures = json.load(f)

# Generate predictions
# Compare with expected output format
```

### For Database Setup
```bash
# Create database
psql -U postgres -c "CREATE DATABASE football_betting_ai;"

# Load schema
psql -U postgres -d football_betting_ai -f test-data/schema.sql

# Import data (using provided import scripts)
```

## Data Generation Methodology

All test data was generated to be:
1. **Statistically realistic** - Follows real football patterns
2. **Internally consistent** - Stats match results
3. **Diverse** - Covers edge cases and normal scenarios
4. **Complete** - All required fields populated
5. **Validated** - Passes data quality checks

## Next Steps

1. Review data structure
2. Adjust if needed for your specific requirements
3. Use for Phase 1 development (data ingestion)
4. Expand as needed for additional markets
