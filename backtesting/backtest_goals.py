"""
Backtest Goals Over 2.5 Model
Walk-forward validation with ROI tracking
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from training.config import TRAINING_DATA_PATHS, BACKTEST_CONFIG, BACKTESTING_RESULTS_DIR
from backtesting.utils import (
    walk_forward_split, calculate_roi, calculate_sharpe_ratio,
    calculate_max_drawdown, print_backtest_summary
)


def walk_forward_backtest_goals(
    data_path: str,
    initial_train_months: int = 12,
    step_months: int = 1,
    min_prob_threshold: float = 0.6
) -> Dict:
    """
    Walk-forward backtest for goals model
    
    Args:
        data_path: Path to training data
        initial_train_months: Initial training period in months
        step_months: Step size in months
        min_prob_threshold: Minimum probability to place bet
        
    Returns:
        Dictionary with backtest results
    """
    print("\n" + "=" * 60)
    print("WALK-FORWARD BACKTEST: GOALS OVER 2.5")
    print("=" * 60)
    
    # Load data
    df = pd.read_csv(data_path)
    df = df.dropna(subset=['y', 'odds_over25'])
    
    # Create walk-forward splits
    splits = walk_forward_split(df, initial_train_months, step_months)
    print(f"📊 Created {len(splits)} walk-forward periods")
    
    # Track results
    all_predictions = []
    all_outcomes = []
    all_odds = []
    period_results = []
    
    for i, (train_df, test_df) in enumerate(splits):
        print(f"\n🔄 Period {i+1}/{len(splits)}")
        print(f"   Train: {len(train_df):,} matches")
        print(f"   Test:  {len(test_df):,} matches")
        
        # Train simple model (for backtesting purposes)
        from sklearn.linear_model import LogisticRegression
        
        exclude_cols = ['match_id', 'date', 'league', 'home_team_id', 
                       'away_team_id', 'y', 'odds_over25']
        feature_cols = [c for c in train_df.columns if c not in exclude_cols]
        
        X_train = train_df[feature_cols].fillna(0)
        y_train = train_df['y'].astype(int)
        
        X_test = test_df[feature_cols].fillna(0)
        y_test = test_df['y'].astype(int)
        test_odds = test_df['odds_over25'].values
        
        # Train model
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train, y_train)
        
        # Predict
        test_proba = model.predict_proba(X_test)[:, 1]
        test_pred = (test_proba >= min_prob_threshold).astype(int)
        
        # Calculate period ROI
        period_roi = calculate_roi(test_pred, y_test.values, test_odds)
        period_results.append(period_roi)
        
        print(f"   Bets:     {period_roi['total_bets']}")
        print(f"   Win Rate: {period_roi['win_rate']:.2%}")
        print(f"   ROI:      {period_roi['roi']:.2f}%")
        
        # Store for overall calculation
        all_predictions.extend(test_pred)
        all_outcomes.extend(y_test.values)
        all_odds.extend(test_odds)
    
    # Calculate overall metrics
    all_predictions = np.array(all_predictions)
    all_outcomes = np.array(all_outcomes)
    all_odds = np.array(all_odds)
    
    overall_roi = calculate_roi(all_predictions, all_outcomes, all_odds)
    
    # Calculate additional metrics
    bet_mask = all_predictions == 1
    if bet_mask.sum() > 0:
        bet_returns = (all_outcomes[bet_mask] * all_odds[bet_mask]) - 1
        sharpe = calculate_sharpe_ratio(bet_returns)
        
        cumulative_returns = np.cumsum(bet_returns)
        max_dd = calculate_max_drawdown(cumulative_returns)
    else:
        sharpe = 0.0
        max_dd = 0.0
    
    results = {
        'total_periods': len(splits),
        'total_bets': overall_roi['total_bets'],
        'win_rate': overall_roi['win_rate'],
        'total_staked': overall_roi['total_staked'],
        'total_return': overall_roi['total_return'],
        'profit': overall_roi['profit'],
        'roi': overall_roi['roi'],
        'sharpe_ratio': sharpe,
        'max_drawdown': max_dd,
        'period_results': period_results
    }
    
    print_backtest_summary(results)
    
    # Save results
    results_df = pd.DataFrame(period_results)
    output_path = BACKTESTING_RESULTS_DIR / 'goals_backtest_summary.csv'
    results_df.to_csv(output_path, index=False)
    print(f"\n💾 Saved results to {output_path}")
    
    return results


def backtest_goals(data_path: str = None):
    """Convenience function for backtesting goals model"""
    if data_path is None:
        data_path = str(TRAINING_DATA_PATHS['goals'])
    
    return walk_forward_backtest_goals(
        data_path,
        initial_train_months=BACKTEST_CONFIG['initial_train_months'],
        step_months=BACKTEST_CONFIG['step_months']
    )


if __name__ == "__main__":
    from typing import Dict
    backtest_goals()
