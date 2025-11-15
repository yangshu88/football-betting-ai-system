"""
Training Module for Football Betting AI System

This module provides comprehensive training infrastructure for all betting markets:
- Data preparation and feature engineering
- Model training with multiple algorithms
- Ensemble and calibration
- Backtesting and evaluation
- Retraining workflows
"""

from .build_datasets import (
    build_training_table_for_goals,
    build_training_table_for_btts,
    build_training_table_for_cards,
    build_training_table_for_corners,
    build_all_training_datasets
)

from .train_goals import train_goals_model
from .train_btts import train_btts_model
from .train_cards import train_cards_model
from .train_corners import train_corners_model

from .utils import (
    fit_calibration_model,
    apply_calibration,
    save_model_with_metadata,
    load_model_with_metadata
)

__all__ = [
    'build_training_table_for_goals',
    'build_training_table_for_btts',
    'build_training_table_for_cards',
    'build_training_table_for_corners',
    'build_all_training_datasets',
    'train_goals_model',
    'train_btts_model',
    'train_cards_model',
    'train_corners_model',
    'fit_calibration_model',
    'apply_calibration',
    'save_model_with_metadata',
    'load_model_with_metadata'
]
