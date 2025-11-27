import json
from .topic import Topic
from utils.file_utils import get_new_topics_file

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
        if not self.topics:
            print("No topics to sort.")
            return

        print("Choose sorting mode:")
        print("1. Ascending")
        print("2. Descending")
        print("3. Middle")

        mode = input("Enter choice (1/2/3): ").strip()

        try:
            sorted_topics = sorted(self.topics, key=lambda t: getattr(t, attribute))
        except AttributeError:
            print(f"Invalid attribute: {attribute}")
            return

        if mode == "1":
            self.topics = sorted_topics

        elif mode == "2":
            self.topics = list(reversed(sorted_topics))

        elif mode == "3":
            mid = len(sorted_topics) // 2

            left = sorted_topics[:mid]
            right = sorted_topics[mid:]

            left = list(reversed(left)) 

            merged = []
            for l, r in zip(left, right):
                merged.append(l)
                merged.append(r)

            if len(left) > len(right):
                merged.extend(left[len(right):])
            elif len(right) > len(left):
                merged.extend(right[len(left):])

            self.topics = merged

        else:
            print("Invalid mode.")
            return

        print(f"\nSorted by {attribute} (mode {mode}):")
        for topic in self.topics:
            print(f"- {topic}")
