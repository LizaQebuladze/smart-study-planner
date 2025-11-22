import json
from topic import Topic

class StudyPlan:
    def __init__(self, file_path = "data/topics.json"):
        self.topics = []
        self.file_path = file_path
    
    def add_topic(self, topic):
        # add a topic object to the study plan
        self.topics.append(topic)
        print(f"Added topic: {topic.name}")

    def remove_topic(self, topic_name):
        # remove topic by its name
        for i, topic in enumerate (self.topics):
            if topic.name.lower() == topic_name.lower():
                self.topics.pop(i)
                print(f"Removed topic: {topic_name.lower()}")
                return
        print(f"No topic with name {topic_name} found")

    def list_topics(self):
        #print all topics
        if not self.topics:
            print("no topics in your study plan yet")
            return
        print("Your study plan topics:")
        for topic in self.topics:
            print(f"- {topic}")
            
    def save(self):
        #save the list of topics to JSON file

        try:
            with open(self.file_path, "w") as f:
                json.dump([t.to_dict() for t in self.topics], f, indent=2)
            print(f"Study plan saved to {self.file_path}")
        except Exception as e:
            print(f"Error saving study plan: {e}")

    def load(self):
        #load topics from JSON into the study plan class
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.topics = [Topic.from_dict(d) for d in data]
            print(f"Loaded {len(self.topics)} topics from {self.file_path}")
        except FileNotFoundError:
            print(f"No saved study plan found at {self.file_path}. Starting fresh.")
        except Exception as e:
            print(f"Error loading study plan: {e}")

    def sort_by(self, attribute):
        # Sort topics by a given attribute (priority, duration, predicted_difficulty, name, etc)
        if not self.topics:
            print("No topics to sort. ")
            return
        try:
            self.topics.sort(key=lambda t: getattr(t, attribute), reverse=True)
            print(f"Topics sorted by {attribute}")
        except AttributeError:
            print(f"Invalid attribute '{attribute}' for sorting. ")
        