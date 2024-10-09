import streamlit as st
from menu import menu

# JSON structure for exercises and mappings
exercise_data = {
    "exercises": {
        "Cloud Hands": {
            "url": "https://youtu.be/4YKqFrA8_Rs",
            "description": "Promotes fluid movement and encourages mindfulness, helping to reduce anxiety and improve mood."
        },
        "Warrior II Pose": {
            "url": "https://youtu.be/Mn6RSIRCV3w",
            "description": "Fosters strength and stability while enhancing confidence and focus, making it effective for improving mood."
        },
        "Zhan Zhuang (Standing Meditation)": {
            "url": "https://youtu.be/yZwdA158sR4",
            "description": "A standing meditation that cultivates inner calm and presence, reducing stress and anxiety."
        },
        "Baduanjin Spinal Twist (Eight Brocades)": {
            "url": "https://youtu.be/4Hg6neT7p4c",
            "description": "Increases flexibility and releases tension, which helps calm the mind and relieve stress."
        },
        "Child's Pose": {
            "url": "https://youtu.be/2MJGg-dUKh0",
            "description": "Encourages relaxation and introspection, providing a sense of safety that can improve emotional well-being."
        },
        "Corpse Pose": {
            "url": "https://youtu.be/bz0aH1706bU",
            "description": "Promotes deep relaxation and mental clarity, helping to alleviate stress and anxiety."
        },
        "Cat-Cow Pose": {
            "url": "https://youtu.be/G9B8qciliKc",
            "description": "Enhances body awareness and encourages a mindful connection between breath and movement, supporting emotional balance."
        },
        "Gentle Neck Stretches": {
            "url": "https://youtu.be/H5h54Q0wpps",
            "description": "Release physical tension and promote relaxation, which can alleviate anxiety and improve mood."
        },
        "Seated Forward Bend": {
            "url": "https://youtu.be/1mwwxcMDDy8",
            "description": "Fosters introspection and calmness, providing a grounding effect that can help reduce stress."
        },
        "Restorative Bridge Pose": {
            "url": "https://youtu.be/52vSL_Z_Zy4",
            "description": "Encourages relaxation and emotional release, contributing to a sense of tranquility."
        },
        "Supported Child's Pose": {
            "url": "https://youtu.be/DK1JRP_4tZ0",
            "description": "Promotes deep relaxation and self-care, helping to reduce anxiety and stress."
        },
        "Tai Chi - Single Whip": {
            "url": "https://youtu.be/1dLchY8R6tU",
            "description": "Enhances mindfulness and focus through graceful movement, reducing stress and improving emotional well-being."
        },
        "Tai Chi - Brush Knee and Twist Step": {
            "url": "https://youtu.be/x_rxOa7f09Y",
            "description": "Fosters balance and mental clarity, aiding in the reduction of anxiety and promoting calmness."
        },
        "Tai Chi - Grasp the Bird's Tail": {
            "url": "https://youtu.be/h1XUftdMPBg",
            "description": "Cultivates mindfulness and fluidity in movement, enhancing mental focus and reducing stress."
        },
        "Baduanjin Holding Up the Heavens": {
            "url": "https://youtu.be/NoYUAXIYLvY",
            "description": "Enhances emotional stability and promotes a sense of calm, helping to reduce anxiety."
        }
    },
    "goals": {
        "Reduce anxiety": [
            "Cloud Hands",
            "Corpse Pose",
            "Zhan Zhuang (Standing Meditation)"
        ],
        "Improve mood": [
            "Cloud Hands",
            "Warrior II Pose",
            "Zhan Zhuang (Standing Meditation)"
        ],
        "Stress relief": [
            "Zhan Zhuang (Standing Meditation)",
            "Corpse Pose",
            "Baduanjin Spinal Twist (Eight Brocades)"
        ],
        "Calm the mind": [
            "Corpse Pose",
            "Zhan Zhuang (Standing Meditation)",
            "Baduanjin Spinal Twist (Eight Brocades)"
        ],
        "Increase mindfulness": [
            "Cloud Hands",
            "Warrior II Pose",
            "Zhan Zhuang (Standing Meditation)"
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

# Form for intake
menu()
st.title("Holistic Exercise Recommendations")

# Add BMI and Protein Calculator Section
st.header("Calculate Your BMI and Protein Intake")

# Create inputs for height, weight, and activity level
height = st.number_input("Enter your height (in cm):", min_value=0, step=1)
weight = st.number_input("Enter your weight (in kg):", min_value=0, step=1)


# Protein intake based on activity level
activity_level = st.selectbox(
    "Select your activity level",
    ["Sedentary", "Moderately active", "Active", "Very active"]
)

# BMI Calculation
if height > 0 and weight > 0:
    height_in_meters = height / 100  # Convert height to meters
    bmi = weight / (height_in_meters ** 2)
    st.write(f"**Your BMI is:** {bmi:.2f}")

    # BMI interpretation
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are in the obese category.")

# Protein Intake Calculation
if weight > 0:
    if activity_level == "Sedentary":
        protein_intake = weight * 0.8
    elif activity_level == "Moderately active":
        protein_intake = weight * 1.2
    elif activity_level == "Active":
        protein_intake = weight * 1.6
    else:
        protein_intake = weight * 2.0

    st.write(f"**Recommended daily protein intake:** {protein_intake:.2f} grams")

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
            title = exercise
            description = exercise_data["exercises"][exercise]["description"]
            video_url = exercise_data["exercises"][exercise]["url"]
            
            if index % 2 == 0:
                with col1:
                    st.write(f"{title} - {description}")
                    st.video(video_url)
            else:
                with col2:
                    st.write(f"{title} - {description}")
                    st.video(video_url)
    else:
        st.write("No matching exercises found for your selections.")
