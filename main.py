from models.study_plan import StudyPlan
from models.topic import Topic
from models.difficulty_model import DifficultyModel
from utils.file_utils import get_new_topics_file

def setup_plan():
    """Setup the study plan for a new or existing user"""
    try:
        print("Welcome! Are you a new user? (y/n)")
        choice = input().strip().lower()
        if choice == "y":
            file_path = get_new_topics_file()
            print(f"Your topics will be stored in {file_path}")
            plan = StudyPlan(file_path=file_path)
        else:
            choice = input("Enter a name of your study plan: ").strip().lower()
            file_path = f"data/{choice}.json"
            plan = StudyPlan(file_path=file_path)
        plan.load()
        return plan
    except Exception as e:
        print(f"Error setting up study plan: {e}")
        return StudyPlan()  # fallback

def main():
    plan = setup_plan()

    try:
        model = DifficultyModel()
    except Exception as e:
        print(f"Error loading difficulty model: {e}")
        model = None

    while True:
        try:
            print("\n=== Smart Study Planner ===")
            print("1. Add topic")
            print("2. Remove topic")
            print("3. List topics")
            print("4. Sort topics")
            print("5. Save and exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                try:
                    name = input("Topic name: ").strip()
                    duration = int(input("Duration in minutes: "))
                    priority = int(input("Priority (number from 1 to 10, 1 the most important and 10 the least important): "))
                    category = input("Category: ").strip()
                    past_scores = input("Past scores (comma-separated, leave blank if none): ")
                    if past_scores:
                        past_scores = [int(s.strip()) for s in past_scores.split(",")]
                    else:
                        past_scores = []

                    topic = Topic(name, duration, priority, category, past_scores, predicted_difficulty=None)

                    if model:
                        topic.predicted_difficulty = model.predict(topic)
                        print(f"Predicted difficulty for '{topic.name}': {topic.predicted_difficulty:.2f}")

                    plan.add_topic(topic)
                except Exception as e:
                    print(f"Error adding topic: {e}")

            elif choice == "2":
                try:
                    name = input("Enter topic name to remove: ").strip()
                    plan.remove_topic(name)
                except Exception as e:
                    print(f"Error removing topic: {e}")

            elif choice == "3":
                try:
                    plan.list_topics()
                except Exception as e:
                    print(f"Error listing topics: {e}")

            elif choice == "4":
                try:
                    attr = input("Sort by (priority, duration, predicted_difficulty, name): ").strip()
                    plan.sort_by(attr)
                except Exception as e:
                    print(f"Error sorting topics: {e}")

            elif choice == "5":
                try:
                    plan.save()
                    print("Goodbye!")
                    break
                except Exception as e:
                    print(f"Error saving study plan: {e}")

            else:
                print("Invalid choice. Try again!")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
