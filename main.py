from models.study_plan import StudyPlan
from models.topic import Topic
from models.difficulty_model import DifficultyModel

def main():
    plan = StudyPlan()
    plan.load()

    model = DifficultyModel()

    while True:
        print("\n=== Smart Study Planner ===")
        print("1. Add topic")
        print("2. Remove topic")
        print("3. List topics")
        print("4. Sort topics")
        print("5. Update predicted difficulty")
        print("6. Save and exit")
        choice = input("Enter choice: ").strip()
    
        if choice == "1":
            name = input("Topic name: ").strip()
            duration = int(input("Duration in minutes: "))
            priority = int(input("Priority (number from 1 to 10):"))
            category = input("Category: ").strip()
            past_scores = input("Past scores (comma-seperated, leave blank if none): ")
            if past_scores:
                past_scores = [int(s.strip() for s in past_scores.split(","))]
            else:
                past_scores = []
        
        elif choice == "2":
            name = input("Enter topic name to remove: ").strip()
            plan.remove_topic(name)
        
        elif choice == "3":
            plan.list_topics()

        elif choice == "4":
            attr = input("Sort by (priority, duration, predicted_difficulty, name): ").strip()
            plan.sort_by(attr)
        
        elif choice == "5":
            model.update_topics(plan.topics)
            print("Updated predicted difficulty for all topics. ")

        elif choice == "6":
            plan.save()

        else:
            print("Invalid choice try again!")

if __name__ == "__main__":
    main()
