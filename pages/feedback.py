import os
import streamlit as st
from PIL import Image

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

USER_ID = 'openai'
APP_ID = 'chat-completion'
MODEL_ID = os.environ.get('VIS_MODEL_ID')
MODEL_VERSION_ID = os.environ.get('VIS_MODEL_VERSION_ID')
PAT = os.environ.get('PAT')

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)
metadata = (('authorization', 'Key ' + PAT),)
userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

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
            post_model_outputs_response = stub.PostModelOutputs(
                service_pb2.PostModelOutputsRequest(
                    user_app_id=userDataObject,
                    model_id=MODEL_ID,
                    version_id=MODEL_VERSION_ID,
                    inputs=[
                        resources_pb2.Input(
                            data=resources_pb2.Data(
                                text=resources_pb2.Text(raw=prompt),
                                image=resources_pb2.Image(base64=bytes_data)
                            )
                        )
                    ]
                ),
                metadata=metadata
            )

            if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
                output = f"Post model outputs failed, status: {post_model_outputs_response.status.description}"
                st.write(output)
            else:
                output = post_model_outputs_response.outputs[0]
                st.markdown(output.data.text.raw)

if __name__ == "__main__":
    main()
