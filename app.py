import streamlit as st

# JSON structure for exercises and mappings
exercise_data = {
    "exercises": {
        "Cloud Hands": "https://www.youtube.com/watch?v=XXXXXXX",
        "Warrior II Pose": "https://www.youtube.com/watch?v=XXXXXXX",
        "Zhan Zhuang (Standing Meditation)": "https://www.youtube.com/watch?v=XXXXXXX",
        "Baduanjin Spinal Twist (Eight Brocades)": "https://www.youtube.com/watch?v=XXXXXXX",
        "Child's Pose": "https://www.youtube.com/watch?v=XXXXXXX",
        "Corpse Pose": "https://www.youtube.com/watch?v=XXXXXXX",
        "Cat-Cow Pose": "https://www.youtube.com/watch?v=XXXXXXX",
        "Gentle Neck Stretches": "https://www.youtube.com/watch?v=XXXXXXX",
        "Seated Forward Bend": "https://www.youtube.com/watch?v=XXXXXXX",
        "Restorative Bridge Pose": "https://www.youtube.com/watch?v=XXXXXXX",
        "Supported Child's Pose": "https://www.youtube.com/watch?v=XXXXXXX",
        "Tai Chi - Single Whip": "https://www.youtube.com/watch?v=XXXXXXX",
        "Tai Chi - Brush Knee and Twist Step": "https://www.youtube.com/watch?v=XXXXXXX",
        "Tai Chi - Grasp the Bird's Tail": "https://www.youtube.com/watch?v=XXXXXXX",
        "Basic Baduanjin Routine": "https://www.youtube.com/watch?v=XXXXXXX",
        "Qigong - Spinal Twist (Spring Forest)": "https://www.youtube.com/watch?v=XXXXXXX"
    },
    "goals": {
        "Improve mental health": [
            "Cloud Hands", "Warrior II Pose", "Zhan Zhuang (Standing Meditation)", "Baduanjin Spinal Twist (Eight Brocades)",
            "Child's Pose", "Corpse Pose", "Cat-Cow Pose"
        ],
        "Physical rehabilitation": ["Gentle Neck Stretches", "Seated Forward Bend", "Restorative Bridge Pose", "Supported Child's Pose"],
        "Increase flexibility": ["Cat-Cow Pose", "Seated Forward Bend", "Cloud Hands"],
        "Enhance strength": ["Warrior II Pose", "Tai Chi - Single Whip", "Tai Chi - Brush Knee and Twist Step"],
        "Stress relief": ["Zhan Zhuang (Standing Meditation)", "Corpse Pose", "Baduanjin Spinal Twist (Eight Brocades)"]
    },
    "mobility": {
        "Limited": ["Restorative Bridge Pose", "Gentle Neck Stretches"],
        "Average": ["Cloud Hands", "Child's Pose", "Tai Chi - Grasp the Bird's Tail"],
        "Good": ["Tai Chi - Single Whip", "Tai Chi - Brush Knee and Twist Step"]
    },
    "experience_level": {
        "Beginner": ["Corpse Pose", "Gentle Neck Stretches", "Supported Child's Pose"],
        "Intermediate": ["Warrior II Pose", "Cloud Hands", "Tai Chi - Single Whip"],
        "Advanced": ["Tai Chi - Brush Knee and Twist Step", "Zhan Zhuang (Standing Meditation)", "Baduanjin Spinal Twist (Eight Brocades)"]
    }
}

# Streamlit form for intake
st.title("Personalized Exercise Recommender")

# User goal selection
st.header("Your Wellness Goals")
selected_goal = st.selectbox(
    "Select your main goal",
    options=list(exercise_data["goals"].keys())
)

# User mobility level
st.header("Your Mobility Level")
mobility_level = st.selectbox(
    "Select your mobility level",
    options=list(exercise_data["mobility"].keys())
)

# User experience level
st.header("Your Experience Level")
experience_level = st.selectbox(
    "Select your experience level",
    options=list(exercise_data["experience_level"].keys())
)

# Recommendations based on input
st.header("Recommended Exercises")
st.write("Based on your input, here are the recommended exercises for you:")

# Display exercises based on user selection
recommended_exercises = set(exercise_data["goals"][selected_goal]) & \
                        set(exercise_data["mobility"][mobility_level]) & \
                        set(exercise_data["experience_level"][experience_level])

if recommended_exercises:
    for exercise in recommended_exercises:
        st.write(f"- {exercise}")
        st.write(f"[Watch here]({exercise_data['exercises'][exercise]})")
else:
    st.write("No matching exercises found for your selections.")
