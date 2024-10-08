import streamlit as st

# JSON structure for exercises and mappings
exercise_data = {
    "exercises": {
        "Cloud Hands": "https://youtu.be/4YKqFrA8_Rs",
        "Warrior II Pose": "https://youtu.be/Mn6RSIRCV3w",
        "Zhan Zhuang (Standing Meditation)": "https://youtu.be/yZwdA158sR4",
        "Baduanjin Spinal Twist (Eight Brocades)": "https://youtu.be/4Hg6neT7p4c",
        "Child's Pose": "https://youtu.be/2MJGg-dUKh0",
        "Corpse Pose": "https://youtu.be/bz0aH1706bU",
        "Cat-Cow Pose": "https://youtu.be/G9B8qciliKc",
        "Gentle Neck Stretches": "https://youtu.be/H5h54Q0wpps",
        "Seated Forward Bend": "https://youtu.be/1mwwxcMDDy8",
        "Restorative Bridge Pose": "https://youtu.be/52vSL_Z_Zy4",
        "Supported Child's Pose": "https://youtu.be/DK1JRP_4tZ0",
        "Tai Chi - Single Whip": "https://youtu.be/1dLchY8R6tU",
        "Tai Chi - Brush Knee and Twist Step": "https://youtu.be/x_rxOa7f09Y",
        "Tai Chi - Grasp the Bird's Tail": "https://youtu.be/h1XUftdMPBg",
        "Baduanjin Holding Up the Heavens": "https://youtu.be/NoYUAXIYLvY"
    },
    "goals": {
        "Reduce anxiety": [
          "Cloud Hands",
          "Corpse Pose",
          "Zhan Zhuang (Standing Meditation)",
          "Baduanjin Spinal Twist (Eight Brocades)",
          "Child's Pose",
          "Cat-Cow Pose"
        ],
        "Improve mood": [
          "Cloud Hands",
          "Warrior II Pose",
          "Zhan Zhuang (Standing Meditation)",
          "Baduanjin Spinal Twist (Eight Brocades)",
          "Cat-Cow Pose",
          "Gentle Neck Stretches"
        ],
        "Stress relief": [
          "Zhan Zhuang (Standing Meditation)",
          "Corpse Pose",
          "Baduanjin Spinal Twist (Eight Brocades)",
          "Cloud Hands",
          "Child's Pose"
        ],
        "Calm the mind": [
          "Corpse Pose",
          "Zhan Zhuang (Standing Meditation)",
          "Baduanjin Spinal Twist (Eight Brocades)",
          "Gentle Neck Stretches"
        ],
        "Increase mindfulness": [
          "Cloud Hands",
          "Warrior II Pose",
          "Zhan Zhuang (Standing Meditation)",
          "Baduanjin Holding Up the Heavens"
        ]
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
st.title("Holistic Exercise Recommender")

with st.form("exercise_form"):
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

    # Submit button
    submit_button = st.form_submit_button("Show Recommended Exercises")

# Recommendations based on input after form submission
if submit_button:
    st.header("Recommended Exercises")
    st.write("Based on your input, here are the recommended exercises for you:")

    # Display exercises based on user selection
    recommended_exercises = set(exercise_data["goals"][selected_goal]) | \
                            set(exercise_data["mobility"][mobility_level]) | \
                            set(exercise_data["experience_level"][experience_level])
    
    if recommended_exercises:
        col1, col2 = st.columns(2)
        for index, exercise in enumerate(recommended_exercises):
            if index % 2 == 0:
                with col1:
                    st.write(f"{exercise}")
                    st.video(exercise_data["exercises"][exercise])
            else:
                with col2:
                    st.write(f"{exercise}")
                    st.video(exercise_data["exercises"][exercise])
    else:
        st.write("No matching exercises found for your selections.")
