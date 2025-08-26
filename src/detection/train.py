from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_model(X_train, y_train, X_test, y_test):
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs('models/trained_models', exist_ok=True)
    joblib.dump(model, 'models/trained_models/malware_detector.pkl')
    return model

# Example usage (assuming prepare_data is run first)
if __name__ == "__main__":
    from src.static_analysis.prepare_features import prepare_data  # Import from static_analysis
    X_train, X_test, y_train, y_test, _ = prepare_data()
    model = train_model(X_train, y_train, X_test, y_test)
