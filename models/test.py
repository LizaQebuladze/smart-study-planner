from topic import Topic
from study_plan import StudyPlan
from difficulty_model import DifficultyModel

plan = StudyPlan()
plan.add_topic(Topic("Graphs", 60, 8, "Math", [80, 90]))
plan.add_topic(Topic("Python OOP", 45, 9, "Programming", [85, 95]))

model = DifficultyModel()
model.update_topics(plan.topics)

for topic in plan.topics:
    print(f"{topic.name} predicted difficulty: {topic.predicted_difficulty:.2f}")
