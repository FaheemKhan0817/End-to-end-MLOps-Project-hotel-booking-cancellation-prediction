from scipy.stats import randint, uniform

LIGHTGM_PARAMS = {
    'n_estimators': randint(100, 1000),          # Increased upper limit for more trees
    'max_depth': randint(5, 100),                # Increased upper limit for deeper trees
    'learning_rate': uniform(0.001, 0.3),        # Wider range for finer control
    'num_leaves': randint(20, 150),              # Increased upper limit for more leaves
    'boosting_type': ['gbdt', 'dart', 'goss'],   # Kept as is, all are viable
    'min_child_samples': randint(10, 50),        # Added to control overfitting
    'subsample': uniform(0.5, 0.5),              # Added: fraction of data per tree (0.5 to 1.0)
    'colsample_bytree': uniform(0.5, 0.5),       # Added: fraction of features per tree (0.5 to 1.0)
    'reg_alpha': uniform(0, 1),                  # Added: L1 regularization
    'reg_lambda': uniform(0, 1),                 # Added: L2 regularization
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 20,          # Increased from 2 to 20 for more exploration
    'cv': 10,              # Increased from 5 to 10 for better validation
    'n_jobs': -1,          # Use all available cores
    'verbose': 2,          # Keep verbosity for progress tracking
    'random_state': 42,    # Keep for reproducibility
    'scoring': 'f1'        # Changed to 'f1' to optimize for F1-Score (or use 'balanced_accuracy' for balance)
}