import json 
import os
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
from topic import Topic

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
DATA_FILE = os.path.join(BASE_DIR, "data", "topics.json")
MODEL_DIR = os.path.join(BASE_DIR, "saved_model")
MODEL_FILE = os.path.join(MODEL_DIR, "difficulty_model.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

with open(DATA_FILE, "r") as f:
    data = json.load(f)

topics = [Topic.from_dict(d) for d in data]

X = []
y = []

for topic in topics:
    avg_score = topic.average_score()
    if topic.predicted_difficulty is not None:
        X.append([topic.average_score(), topic.duration, topic.priority])
        y.append(topic.predicted_difficulty)
    

X = np.array(X)
y = np.array(y)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)


joblib.dump(model, MODEL_FILE)
print(f"Trained model saved to {MODEL_FILE}")