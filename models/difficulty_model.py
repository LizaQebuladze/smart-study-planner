from sklearn.ensemble import RandomForestRegressor
import os
import joblib
import numpy as np
from models.topic import Topic
class DifficultyModel:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model_path = os.path.join(BASE_DIR, "saved_model", "difficulty_model.pkl")

        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"Loaded model from {self.model_path}")
        else:
            self.model = None
            print("No saved model found. Please train the model first.")

    def predict(self, topic: Topic):
        if not self.model:
            print("No trained model available. Cannot predict difficulty.")
            return None
        
        features = np.array([[topic.average_score(), topic.duration, topic.priority]])
        predicted = float(self.model.predict(features)[0])
        return predicted

    def update_topics(self, topics):
        # update predicted_difficulty for all topics
        if not self.model:
            print("No trained model available. Cannot update topics.")
            return

        for topic in topics:
            topic.predicted_difficulty = self.predict(topic)

        
