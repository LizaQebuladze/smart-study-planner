class topic:
    def __init__(self, name, duration, priority, category, past_scores=None, predicted_difficulty=None):
        self.name = name   #topic title
        self.duration = duration  #estimated study time in minutes
        self.priority = priority   #1-10, 1 the least important and 10 the most important
        self.category = category
        self.past_scores = past_scores if past_scores is not None else [] #each score between 0-100
        self.predicted_difficulty = predicted_difficulty
    
    def average_score(self):
        if not self.past_scores:
            return 0.0
        else: 
            return sum(self.past_scores) / len(self.past_scores)

    def __str__(self):
        return f"{self.name} ({self.category}) - Duration: {self.duration} min, Priority: {self.priority}, Average score: {self.average_score():.2f}"

    def to_dict(self):
        # converting the topic object to a dictionay for JSON saving
        return {
            "name": self.name,
            "duration": self.duration,
            "priority": self.priority,
            "category": self.category,
            "past_scores": self.past_scores,
            "predicted_difficulty": self.predicted_difficulty
        }
    
    @classmethod
    def from_dict(cls, data):
        # create a topic object from a dictionary loaded from JSON file 
        return cls(
            name = data.get("name"),
            duration = data.get("duration"),
            priority = data.get("priority"),
            category = data.get("category"),
            past_scores = data.get("past_scores", []),
            predicted_difficulty = data.get("predicted_difficulty")
        )