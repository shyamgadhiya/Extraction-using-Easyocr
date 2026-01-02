import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from feature_engineering import extract_features

# Load data
df = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\text_to_csv_columns.csv")

X = df["text"].apply(extract_features).tolist()
y = df["label"]

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved")
