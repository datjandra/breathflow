import os
import streamlit as st
from PIL import Image

from clarifai.client.model import Model
from clarifai.client.input import Inputs

# JSON-like object to store posture details
posture_details = {
    "Zhan Zhuang": {
        "image_path": "https://i0.wp.com/wanderingfist.wordpress.com/wp-content/uploads/2015/12/hanxingqiao3.jpg",
        "prompt": "Does the image show a correct zhan zhuang posture?",
        "description": """
            Zhan Zhuang, or "standing like a tree", improves posture, balance, internal strength, mental focus, and overall vitality through sustained, meditative standing.
        """
    },
    "Corpse Pose": {
        "image_path": "https://www.keralatourism.org/images/yoga/static-banner/large/Savasana_-_The_Corpse_Pose-07032020145736.jpg"
        "prompt": "Does the image show a correct corpse pose?",
        "description": """
            The Corpse Pose (Savasana) promotes deep relaxation by calming the mind, reducing stress, and helping the body recover after practice.
        """
    },
    "Warrior II Pose": {
        "image_path": "https://cdn.yogajournal.com/wp-content/uploads/2021/12/Warrior-2-Pose_Andrew-Clark_2400x1350.jpeg"
        "prompt": "Does the image show a correct warrior 2 pose?",
        "description": """
            The Warrior II Pose (Virabhadrasana II) strengthens the legs and core while enhancing focus and mental endurance, promoting balance between physical power and mental clarity.
        """
    }
}

def main():
    st.set_page_config(page_title="Posture Analysis")
    st.title("Posture Analysis")

    st.markdown("""
        ## Introduction to Posture Analysis
        
        This page analyzes various postures, specifically focusing on practices for mind and body health benefits.
    """)
    
    # Select box for the posture type
    posture_type = st.selectbox(
        "Select the type of posture for analysis:",
        list(posture_details.keys()),
        index=0
    )

    # Get posture details from the JSON object
    selected_posture = posture_details[posture_type]
    description = selected_posture["description"]
    image_path = selected_posture["image_path"]
    prompt = selected_posture["prompt"]

    # Display posture description and example image
    st.markdown(f"### {posture_type}")
    st.markdown(description)

    st.image(image_path, caption=f"Example: {posture_type} Posture", use_column_width=True)

    # Uploading user image for analysis
    uploaded_file = st.file_uploader("Please upload a picture of your standing posture.", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        if image is not None:
            st.image(image, caption="Uploaded Posture Image", use_column_width=True)

        bytes_data = uploaded_file.getvalue()
        with st.spinner('Analyzing image of posture...'):

            # prompt = "What time of day is it?"
            # image_url = "https://samples.clarifai.com/metro-north.jpg"
            
            inference_params = dict(temperature=0.2, max_tokens=256, top_p=0.9)
            model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4o").predict(inputs = [Inputs.get_multimodal_input(input_id="", image_bytes=bytes_data, raw_text=prompt)], inference_params=inference_params)
            st.markdown(model_prediction.outputs[0].data.text.raw)

if __name__ == "__main__":
    main()
