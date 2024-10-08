import os
import streamlit as st
from PIL import Image

from clarifai.client.model import Model
from clarifai.client.input import Inputs

# JSON-like object to store posture details
posture_details = {
    "Zhan Zhuang": {
        "image_path": "https://i0.wp.com/wanderingfist.wordpress.com/wp-content/uploads/2015/12/hanxingqiao3.jpg",  # Replace with actual path or URL
        "prompt": os.getenv('VIS_ZZ_PROMPT'),
        "description": """
            Zhan Zhuang, or "standing like a tree", improves posture, balance, internal strength, mental focus, and overall vitality through sustained, meditative standing.
        """
    },
    "Santi Shi": {
        "image_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiDH08_U8-iqUwX6Y5Ziwf3w7bF0DszjdayA&s",  # Replace with actual path or URL
        "prompt": os.getenv('VIS_STS_PROMPT'),
        "description": """
            Santi Shi, or "three body posture", enhances balance, core and leg strength, flexibility, mental focus, and overall vitality.
        """
    }
}

def main():
    st.set_page_config(page_title="Posture Analysis")
    st.title("Standing Posture Analysis")

    st.markdown("""
        ## Introduction to Standing Postures
        
        This page analyzes your standing postures, specifically focusing on two practices for health benefits: [Zhan Zhuang](https://en.wikipedia.org/wiki/Zhan_zhuang) and [Santi Shi](https://en.wikipedia.org/wiki/Xingyiquan).
    """)

    # Select box for the posture type
    posture_type = st.selectbox(
        "Select the type of standing posture for analysis:",
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
            inference_params = dict(temperature=0.2, max_tokens=256, top_p=0.9)
            model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4o").predict(inputs = [Inputs.get_multimodal_input(input_id="", image_bytes=bytes_data, raw_text=prompt)], inference_params=inference_params)
            st.markdown(model_prediction.outputs[0].data.text.raw)

if __name__ == "__main__":
    main()
