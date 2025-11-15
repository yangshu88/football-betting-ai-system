"""
Retrain All Models Script
Automated retraining workflow for all markets
"""

import sys
from pathlib import Path
from datetime import datetime
import json

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from training.build_datasets import build_all_training_datasets
from training.train_goals import train_goals_model
from training.train_btts import train_btts_model
from training.train_cards import train_cards_model
from training.train_corners import train_corners_model
from training.config import (
    RETRAIN_CONFIG, MODELS_DIR, TRAINING_DATA_PATHS
)
from training.utils import increment_version


def check_retraining_needed() -> bool:
    """
    Check if retraining is needed based on configuration
    
    Returns:
        True if retraining should proceed
    """
    # Check if enough new data is available
    # This is a simplified check - in production, query database for new matches
    
    print("🔍 Checking if retraining is needed...")
    
    # For now, always return True (manual trigger)
    # In production, implement logic to check:
    # - Number of new matches since last training
    # - Model performance degradation
    # - Time since last training
    
    return True


def validate_model_performance(market: str, metrics: Dict) -> bool:
    """
    Validate that new model meets performance thresholds
    
    Args:
        market: Market name
        metrics: Dictionary with model metrics
        
    Returns:
        True if model meets thresholds
    """
    thresholds = RETRAIN_CONFIG['performance_threshold']
    
    log_loss = metrics.get('log_loss', float('inf'))
    brier_score = metrics.get('brier_score', float('inf'))
    
    if log_loss > thresholds['log_loss']:
        print(f"⚠️  {market}: Log loss {log_loss:.4f} exceeds threshold {thresholds['log_loss']}")
        return False
    
    if brier_score > thresholds['brier_score']:
        print(f"⚠️  {market}: Brier score {brier_score:.4f} exceeds threshold {thresholds['brier_score']}")
        return False
    
    return True


def promote_model(market: str, new_version: str):
    """
    Promote new model to active version
    
    Args:
        market: Market name
        new_version: New version string
    """
    market_dir = MODELS_DIR / market
    
    # Update active model pointer
    active_config = {
        'active_version': new_version,
        'promoted_at': datetime.now().isoformat(),
        'status': 'active'
    }
    
    active_path = market_dir / 'active_model.json'
    with open(active_path, 'w') as f:
        json.dump(active_config, f, indent=2)
    
    print(f"✅ Promoted {market} model to version {new_version}")


def retrain_all_models(force: bool = False):
    """
    Main retraining workflow
    
    Args:
        force: Force retraining even if not needed
    """
    print("\n" + "=" * 60)
    print("AUTOMATED MODEL RETRAINING WORKFLOW")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check if retraining is needed
    if not force and not check_retraining_needed():
        print("✅ Retraining not needed at this time")
        return
    
    # Step 1: Build fresh training datasets
    print("\n📊 Step 1: Building training datasets...")
    try:
        build_all_training_datasets()
    except Exception as e:
        print(f"❌ Error building datasets: {e}")
        return
    
    # Step 2: Train models for each market
    markets = ['goals', 'btts', 'cards', 'corners']
    training_functions = {
        'goals': train_goals_model,
        'btts': train_btts_model,
        'cards': train_cards_model,
        'corners': train_corners_model
    }
    
    results = {}
    
    for market in markets:
        print(f"\n📊 Step 2.{markets.index(market)+1}: Training {market} model...")
        
        try:
            result = training_functions[market]()
            results[market] = result
            
            # Validate performance
            test_metrics = result.get('test_metrics', {})
            if validate_model_performance(market, test_metrics):
                # Get current version and increment
                market_dir = MODELS_DIR / market
                ensemble_meta_path = market_dir / 'ensemble_metadata.json'
                
                if ensemble_meta_path.exists():
                    with open(ensemble_meta_path, 'r') as f:
                        metadata = json.load(f)
                    current_version = metadata.get('version', 'v1.0.0')
                else:
                    current_version = 'v1.0.0'
                
                new_version = increment_version(
                    current_version, 
                    RETRAIN_CONFIG['version_increment']
                )
                
                # Update version in metadata
                if ensemble_meta_path.exists():
                    with open(ensemble_meta_path, 'r') as f:
                        metadata = json.load(f)
                    metadata['version'] = new_version
                    metadata['retrained_at'] = datetime.now().isoformat()
                    with open(ensemble_meta_path, 'w') as f:
                        json.dump(metadata, f, indent=2)
                
                # Promote model
                promote_model(market, new_version)
            else:
                print(f"⚠️  {market} model did not meet performance thresholds - not promoted")
        
        except Exception as e:
            print(f"❌ Error training {market} model: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    # Step 3: Summary
    print("\n" + "=" * 60)
    print("RETRAINING SUMMARY")
    print("=" * 60)
    
    for market, result in results.items():
        if result:
            test_metrics = result.get('test_metrics', {})
            print(f"\n{market.upper()}:")
            print(f"  Log Loss:    {test_metrics.get('log_loss', 'N/A')}")
            print(f"  Brier Score: {test_metrics.get('brier_score', 'N/A')}")
            print(f"  Accuracy:    {test_metrics.get('accuracy', 'N/A')}")
    
    print("\n" + "=" * 60)
    print(f"✅ RETRAINING COMPLETE")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Retrain all betting models')
    parser.add_argument('--force', action='store_true', 
                       help='Force retraining even if not needed')
    
    args = parser.parse_args()
    
    retrain_all_models(force=args.force)
