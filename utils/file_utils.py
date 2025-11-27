import os
def get_new_topics_file(base_dir="data", prefix="topics", ext=".json"):
    i = 1
    while True:
        new_file = os.path.join(base_dir, f"{prefix}{i}{ext}")
        if not os.path.exists(new_file):
            return new_file
        i += 1