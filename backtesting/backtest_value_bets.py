"""
Backtest Value Bets Strategy
Tests value betting approach with Kelly criterion staking
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backtesting.utils import calculate_kelly_stake, print_backtest_summary
from training.config import BACKTESTING_RESULTS_DIR


def backtest_value_bets(
    data_path: str,
    min_value_pct: float = 5.0,
    initial_bankroll: float = 1000.0,
    kelly_fraction: float = 0.25
) -> Dict:
    """
    Backtest value betting strategy with Kelly staking
    
    Args:
        data_path: Path to data with predictions and odds
        min_value_pct: Minimum value percentage to place bet
        initial_bankroll: Starting bankroll
        kelly_fraction: Fraction of Kelly to use
        
    Returns:
        Dictionary with backtest results
    """
    print("\n" + "=" * 60)
    print("VALUE BETS BACKTEST")
    print("=" * 60)
    
    df = pd.read_csv(data_path)
    df = df.dropna(subset=['y', 'odds_over25'])
    
    # Simulate predictions (in real scenario, use actual model predictions)
    # For demo, use simple probability estimates
    df['ai_prob'] = 0.5  # Placeholder
    df['implied_prob'] = 1 / df['odds_over25']
    df['value_pct'] = ((df['ai_prob'] / df['implied_prob']) - 1) * 100
    
    # Filter value bets
    value_bets = df[df['value_pct'] >= min_value_pct].copy()
    
    print(f"📊 Total matches: {len(df):,}")
    print(f"📊 Value bets found: {len(value_bets):,} ({len(value_bets)/len(df):.1%})")
    
    if len(value_bets) == 0:
        print("❌ No value bets found!")
        return {}
    
    # Simulate betting with Kelly criterion
    bankroll = initial_bankroll
    bankroll_history = [bankroll]
    
    total_staked = 0
    total_return = 0
    wins = 0
    
    for idx, row in value_bets.iterrows():
        # Calculate Kelly stake
        stake = calculate_kelly_stake(
            row['ai_prob'], row['odds_over25'], bankroll, kelly_fraction
        )
        
        # Place bet
        total_staked += stake
        
        if row['y'] == 1:  # Win
            returns = stake * row['odds_over25']
            bankroll += (returns - stake)
            total_return += returns
            wins += 1
        else:  # Loss
            bankroll -= stake
        
        bankroll_history.append(bankroll)
    
    # Calculate metrics
    profit = bankroll - initial_bankroll
    roi = (profit / total_staked) * 100 if total_staked > 0 else 0
    win_rate = wins / len(value_bets)
    
    # Calculate max drawdown
    bankroll_array = np.array(bankroll_history)
    running_max = np.maximum.accumulate(bankroll_array)
    drawdown = (bankroll_array - running_max) / running_max
    max_drawdown = drawdown.min() * 100
    
    results = {
        'total_bets': len(value_bets),
        'win_rate': win_rate,
        'total_staked': total_staked,
        'total_return': total_return,
        'profit': profit,
        'roi': roi,
        'final_bankroll': bankroll,
        'max_drawdown': max_drawdown,
        'initial_bankroll': initial_bankroll
    }
    
    print_backtest_summary(results)
    print(f"Initial Bankroll: ${initial_bankroll:,.2f}")
    print(f"Final Bankroll:   ${bankroll:,.2f}")
    
    # Save results
    results_df = pd.DataFrame([results])
    output_path = BACKTESTING_RESULTS_DIR / 'value_bets_backtest_summary.csv'
    results_df.to_csv(output_path, index=False)
    print(f"\n💾 Saved results to {output_path}")
    
    return results


if __name__ == "__main__":
    from typing import Dict
    from training.config import TRAINING_DATA_PATHS
    backtest_value_bets(str(TRAINING_DATA_PATHS['goals']))
