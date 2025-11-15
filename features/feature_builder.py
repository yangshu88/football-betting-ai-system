"""
Centralized Feature Builder
Ensures training and inference use identical feature engineering logic
"""

import pandas as pd
import numpy as np
from typing import Dict, List


class FeatureBuilder:
    """
    Centralized feature engineering for both training and prediction
    Ensures consistency between training and inference
    """
    
    def __init__(self):
        self.feature_columns = []
    
    def build_features(self, match_data: Dict) -> Dict:
        """
        Build features from match data dictionary
        
        Args:
            match_data: Dictionary with match information and team stats
            
        Returns:
            Dictionary with engineered features
        """
        features = {}
        
        # Extract base stats
        home_goals_avg = match_data.get('home_goals_avg_5', match_data.get('home_goals_avg', 0))
        away_goals_avg = match_data.get('away_goals_avg_5', match_data.get('away_goals_avg', 0))
        home_goals_conceded_avg = match_data.get('home_goals_conceded_avg_5', 
                                                 match_data.get('home_goals_conceded_avg', 0))
        away_goals_conceded_avg = match_data.get('away_goals_conceded_avg_5',
                                                 match_data.get('away_goals_conceded_avg', 0))
        home_corners_avg = match_data.get('home_corners_avg_5', match_data.get('home_corners_avg', 0))
        away_corners_avg = match_data.get('away_corners_avg_5', match_data.get('away_corners_avg', 0))
        home_cards_avg = match_data.get('home_cards_avg_5', match_data.get('home_cards_avg', 0))
        away_cards_avg = match_data.get('away_cards_avg_5', match_data.get('away_cards_avg', 0))
        home_btts_rate = match_data.get('home_btts_rate_5', match_data.get('home_btts_rate', 0))
        away_btts_rate = match_data.get('away_btts_rate_5', match_data.get('away_btts_rate', 0))
        
        # Basic features
        features['home_goals_avg_5'] = home_goals_avg
        features['away_goals_avg_5'] = away_goals_avg
        features['home_goals_conceded_avg_5'] = home_goals_conceded_avg
        features['away_goals_conceded_avg_5'] = away_goals_conceded_avg
        features['home_corners_avg_5'] = home_corners_avg
        features['away_corners_avg_5'] = away_corners_avg
        features['home_cards_avg_5'] = home_cards_avg
        features['away_cards_avg_5'] = away_cards_avg
        features['home_btts_rate_5'] = home_btts_rate
        features['away_btts_rate_5'] = away_btts_rate
        
        # 10-match averages (if available)
        features['home_goals_avg_10'] = match_data.get('home_goals_avg_10', home_goals_avg)
        features['away_goals_avg_10'] = match_data.get('away_goals_avg_10', away_goals_avg)
        features['home_goals_conceded_avg_10'] = match_data.get('home_goals_conceded_avg_10', 
                                                                home_goals_conceded_avg)
        features['away_goals_conceded_avg_10'] = match_data.get('away_goals_conceded_avg_10',
                                                                away_goals_conceded_avg)
        
        # Combined features
        features['combined_goals_avg'] = home_goals_avg + away_goals_avg
        features['combined_corners_avg'] = home_corners_avg + away_corners_avg
        features['combined_cards_avg'] = home_cards_avg + away_cards_avg
        features['combined_btts_rate'] = (home_btts_rate + away_btts_rate) / 2
        
        # Attack vs Defense
        features['home_attack_vs_away_defense'] = home_goals_avg - away_goals_conceded_avg
        features['away_attack_vs_home_defense'] = away_goals_avg - home_goals_conceded_avg
        
        return features
    
    def build_features_batch(self, matches: List[Dict]) -> pd.DataFrame:
        """
        Build features for multiple matches
        
        Args:
            matches: List of match dictionaries
            
        Returns:
            DataFrame with features
        """
        features_list = [self.build_features(match) for match in matches]
        return pd.DataFrame(features_list)
    
    def get_feature_names(self) -> List[str]:
        """Get list of feature names"""
        return [
            'home_goals_avg_5', 'away_goals_avg_5',
            'home_goals_conceded_avg_5', 'away_goals_conceded_avg_5',
            'home_corners_avg_5', 'away_corners_avg_5',
            'home_cards_avg_5', 'away_cards_avg_5',
            'home_btts_rate_5', 'away_btts_rate_5',
            'home_goals_avg_10', 'away_goals_avg_10',
            'home_goals_conceded_avg_10', 'away_goals_conceded_avg_10',
            'combined_goals_avg', 'combined_corners_avg',
            'combined_cards_avg', 'combined_btts_rate',
            'home_attack_vs_away_defense', 'away_attack_vs_home_defense'
        ]
