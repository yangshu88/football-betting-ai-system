#!/usr/bin/env python3
"""
Generate complete test dataset for Football Betting AI System
Run this script to create:
- 300 historical matches
- 200 upcoming fixtures
- 400 team statistics
"""

import json
import random
from datetime import datetime, timedelta

# Load teams
with open('teams.json', 'r') as f:
    teams_data = json.load(f)
    teams = teams_data['teams']

def generate_team_stats():
    """Generate realistic team statistics"""
    return {
        "home_goals_avg": round(random.uniform(1.0, 2.5), 1),
        "away_goals_avg": round(random.uniform(0.8, 2.0), 1),
        "home_goals_conceded_avg": round(random.uniform(0.6, 1.6), 1),
        "away_goals_conceded_avg": round(random.uniform(0.8, 1.8), 1),
        "home_corners_avg": round(random.uniform(4.5, 8.5), 1),
        "away_corners_avg": round(random.uniform(4.0, 7.0), 1),
        "home_cards_avg": round(random.uniform(1.5, 2.8), 1),
        "away_cards_avg": round(random.uniform(1.7, 3.0), 1),
        "home_btts_rate": round(random.uniform(0.40, 0.70), 2),
        "away_btts_rate": round(random.uniform(0.45, 0.75), 2),
        "home_form": ''.join(random.choices(['W', 'D', 'L'], weights=[0.50, 0.25, 0.25], k=5)),
        "away_form": ''.join(random.choices(['W', 'D', 'L'], weights=[0.30, 0.25, 0.45], k=5))
    }

def generate_odds():
    """Generate realistic betting odds"""
    home_strength = random.uniform(0.3, 0.7)
    
    if home_strength > 0.6:
        home_win = round(random.uniform(1.30, 1.80), 2)
        away_win = round(random.uniform(5.00, 9.00), 2)
    elif home_strength < 0.4:
        home_win = round(random.uniform(3.50, 7.00), 2)
        away_win = round(random.uniform(1.40, 2.20), 2)
    else:
        home_win = round(random.uniform(1.90, 3.00), 2)
        away_win = round(random.uniform(2.20, 4.50), 2)
    
    draw = round(random.uniform(3.20, 4.50), 2)
    
    return {
        "home_win": home_win,
        "draw": draw,
        "away_win": away_win,
        "over_0_5": round(random.uniform(1.02, 1.08), 2),
        "under_0_5": round(random.uniform(10.00, 18.00), 2),
        "over_1_5": round(random.uniform(1.15, 1.35), 2),
        "under_1_5": round(random.uniform(3.50, 5.50), 2),
        "over_2_5": round(random.uniform(1.65, 2.20), 2),
        "under_2_5": round(random.uniform(1.70, 2.30), 2),
        "over_3_5": round(random.uniform(2.80, 3.80), 2),
        "under_3_5": round(random.uniform(1.25, 1.45), 2),
        "over_4_5": round(random.uniform(5.50, 8.00), 2),
        "under_4_5": round(random.uniform(1.06, 1.15), 2),
        "btts_yes": round(random.uniform(1.60, 2.20), 2),
        "btts_no": round(random.uniform(1.70, 2.30), 2),
        "home_or_draw": round(1 / (1/home_win + 1/draw), 2),
        "away_or_draw": round(1 / (1/away_win + 1/draw), 2),
        "home_or_away": round(1 / (1/home_win + 1/away_win), 2),
        "corners_over_8_5": round(random.uniform(1.50, 1.90), 2),
        "corners_under_8_5": round(random.uniform(1.95, 2.60), 2),
        "corners_over_9_5": round(random.uniform(1.80, 2.25), 2),
        "corners_under_9_5": round(random.uniform(1.65, 2.10), 2),
        "corners_over_10_5": round(random.uniform(2.25, 2.85), 2),
        "corners_under_10_5": round(random.uniform(1.45, 1.70), 2),
        "cards_over_3_5": round(random.uniform(2.00, 2.30), 2),
        "cards_under_3_5": round(random.uniform(1.65, 1.85), 2),
        "cards_over_4_5": round(random.uniform(3.00, 3.70), 2),
        "cards_under_4_5": round(random.uniform(1.28, 1.42), 2)
    }

def generate_result():
    """Generate realistic match result"""
    result_type = random.choices(['home_win', 'draw', 'away_win'], weights=[0.45, 0.25, 0.30])[0]
    
    if result_type == 'home_win':
        home_goals = random.randint(2, 4)
        away_goals = random.randint(0, home_goals - 1)
    elif result_type == 'draw':
        goals = random.randint(0, 3)
        home_goals = away_goals = goals
    else:
        away_goals = random.randint(2, 4)
        home_goals = random.randint(0, away_goals - 1)
    
    total_goals = home_goals + away_goals
    total_corners = random.randint(7, 15)
    total_cards = random.randint(2, 6)
    
    return {
        "home_goals": home_goals,
        "away_goals": away_goals,
        "result": result_type,
        "total_goals": total_goals,
        "home_corners": random.randint(int(total_corners * 0.4), int(total_corners * 0.7)),
        "away_corners": total_corners - random.randint(int(total_corners * 0.4), int(total_corners * 0.7)),
        "total_corners": total_corners,
        "home_cards": random.randint(1, 4),
        "away_cards": random.randint(1, 4),
        "total_cards": total_cards,
        "btts": home_goals > 0 and away_goals > 0,
        "over_0_5": total_goals > 0,
        "over_1_5": total_goals > 1,
        "over_2_5": total_goals > 2,
        "over_3_5": total_goals > 3,
        "over_4_5": total_goals > 4,
        "corners_over_8_5": total_corners > 8,
        "corners_over_9_5": total_corners > 9,
        "corners_over_10_5": total_corners > 10,
        "cards_over_3_5": total_cards > 3,
        "cards_over_4_5": total_cards > 4
    }

def generate_historical_matches(count=300):
    """Generate historical matches"""
    matches = []
    start_date = datetime(2022, 1, 1)
    
    for i in range(count):
        match_date = start_date + timedelta(days=random.randint(0, 1050))
        home_team = random.choice(teams)
        away_team = random.choice([t for t in teams if t['team_id'] != home_team['team_id']])
        
        match = {
            "match_id": f"HM_{match_date.year}_{i+1:03d}",
            "match_datetime": match_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "season": f"{match_date.year}-{(match_date.year % 100) + 1:02d}",
            "league": home_team['league'],
            "status": "completed",
            "home_team_id": home_team['team_id'],
            "home_team": home_team['team_name'],
            "away_team_id": away_team['team_id'],
            "away_team": away_team['team_name'],
            "team_stats_at_match_time": generate_team_stats(),
            "odds": generate_odds(),
            "result": generate_result()
        }
        matches.append(match)
    
    return matches

def generate_upcoming_fixtures(count=200):
    """Generate upcoming fixtures"""
    fixtures = []
    match_date = datetime(2025, 11, 16, 15, 0, 0)  # Saturday 3pm
    
    for i in range(count):
        home_team = random.choice(teams)
        away_team = random.choice([t for t in teams if t['team_id'] != home_team['team_id']])
        
        fixture = {
            "match_id": f"UF_{i+1:03d}",
            "match_datetime": match_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "league": home_team['league'],
            "home_team_id": home_team['team_id'],
            "home_team": home_team['team_name'],
            "away_team_id": away_team['team_id'],
            "away_team": away_team['team_name'],
            "team_stats_at_match_time": generate_team_stats(),
            "odds": generate_odds()
        }
        fixtures.append(fixture)
        
        # Vary kickoff times slightly
        if (i + 1) % 10 == 0:
            match_date += timedelta(hours=2, minutes=30)
    
    return fixtures

def generate_team_statistics():
    """Generate team statistics for all 400 teams"""
    stats = []
    for team in teams:
        stat = {
            "team_id": team['team_id'],
            "team_name": team['team_name'],
            "league": team['league'],
            "season": "2024-25",
            "matches_played": random.randint(10, 15),
            "wins": random.randint(3, 10),
            "draws": random.randint(1, 5),
            "losses": random.randint(1, 7),
            "goals_scored": random.randint(12, 30),
            "goals_conceded": random.randint(8, 25),
            "home_goals_avg": round(random.uniform(1.0, 2.5), 2),
            "away_goals_avg": round(random.uniform(0.8, 2.0), 2),
            "home_goals_conceded_avg": round(random.uniform(0.6, 1.6), 2),
            "away_goals_conceded_avg": round(random.uniform(0.8, 1.8), 2),
            "corners_avg": round(random.uniform(4.5, 7.5), 1),
            "cards_avg": round(random.uniform(1.8, 2.8), 1),
            "btts_rate": round(random.uniform(0.40, 0.70), 2),
            "over_2_5_rate": round(random.uniform(0.40, 0.65), 2),
            "form_last_5": ''.join(random.choices(['W', 'D', 'L'], weights=[0.40, 0.25, 0.35], k=5))
        }
        stats.append(stat)
    
    return stats

# Generate all datasets
print("Generating 300 historical matches...")
historical = generate_historical_matches(300)

print("Generating 200 upcoming fixtures...")
fixtures = generate_upcoming_fixtures(200)

print("Generating 400 team statistics...")
team_stats = generate_team_statistics()

# Save to files
print("Saving historical_matches_300.json...")
with open('historical_matches_300_generated.json', 'w') as f:
    json.dump({
        "metadata": {
            "description": "Complete historical match data for AI model training",
            "total_matches": 300,
            "date_range": "2022-01-01 to 2025-11-14",
            "distribution": {"2022": 100, "2023": 100, "2024-2025": 100},
            "betting_markets_covered": ["match_result", "total_goals", "btts", "double_chance", "corners", "cards"],
            "note": "Generated realistic fake data for testing"
        },
        "matches": historical
    }, f, indent=2)

print("Saving upcoming_fixtures_200.json...")
with open('upcoming_fixtures_200_generated.json', 'w') as f:
    json.dump({
        "metadata": {
            "description": "Upcoming fixtures for prediction testing - Busy Saturday",
            "total_fixtures": 200,
            "date_range": "2025-11-16 (Saturday)",
            "note": "No results - for generating predictions"
        },
        "fixtures": fixtures
    }, f, indent=2)

print("Saving team_statistics_400.json...")
with open('team_statistics_400_generated.json', 'w') as f:
    json.dump({
        "metadata": {
            "description": "Team statistics for all 400 teams",
            "season": "2024-25",
            "total_teams": 400
        },
        "statistics": team_stats
    }, f, indent=2)

print("\n✅ Complete! Generated:")
print("  - historical_matches_300_generated.json")
print("  - upcoming_fixtures_200_generated.json")
print("  - team_statistics_400_generated.json")
