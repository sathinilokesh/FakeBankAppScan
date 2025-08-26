import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def prepare_data(csv_path='data/processed/lamda_subset.csv', test_size=0.2):
    df = pd.read_csv(csv_path)
    
    # Features are feat_0 to feat_4560, label is 'label'
    feature_cols = [col for col in df.columns if col.startswith('feat_')]
    X = df[feature_cols].values
    y = df['label'].values
    
    # Scale features (important for ML)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split (though LAMDA has pre-splits, we can re-split for customization)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, stratify=y, random_state=42)
    
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    return X_train, X_test, y_train, y_test, scaler

# Example usage
if __name__ == "__main__":
    X_train, X_test, y_train, y_test, _ = prepare_data()
