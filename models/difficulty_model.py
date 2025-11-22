from sklearn.ensemble import RandomForestRegressor
import numpy as np
class DifficultyModel:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=50, random_state=42)
        self.trained = False

    def _prepare_features(self, topic):
        """
        convert a topic object into a feature vector:
        - average past score
        - duration in minutes
        - priority (1-10)
        """

        avg_score = topic.average_score()
        duration = topic.duration
        priority = topic.priority
        
        return np.array([[avg_score, duration, priority]])
    
    def train (self, topics):
        #train model on the list of topics known predicted_difficulty

        X = []
        y = []
        for topic in topics:
            if topic.predicted_difficulty is not None:
                X.append([topic.average_score(), topic.duration, topic.priority])
                y.append(topic.predicted_difficulty)

            if X and y:
                self.model.fit(X,y)
                self.trained = True
                print(f"Difficulty model trained on {len(X)} topics. ")
            else:
                print(f"No topics with known difficulty to train model. ")

    def predict(self, topic):
        # predict difficulty for a single topic and return float

        features = self._prepare_features(topic)
        if self.trained:
            predicted = self.model.predict(features)[0]
        else :
            predicted = max(0, min(10, 10-topic.average_score() / 10 + topic.duration /60))
        return predicted
    
    def update_topics(self, topics):
        # update predicted_difficulty for all topics
        for topic in topics:
            topic.predicted_difficulty = self.predict(topic)

        
