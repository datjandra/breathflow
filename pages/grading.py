import os
import time
import requests
import io

import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from twelvelabs import TwelveLabs
from twelvelabs.models.embed import EmbeddingsTask

import numpy as np
from numpy.linalg import norm

from menu import menu

TL_API_KEY = os.getenv('TL_API_KEY')

# Mapping between video names and corresponding embedding URLs
video_options = {
  "Yang Jun - Cloud Hands": {
      "video_url": "https://youtu.be/PrmMJWxGT44",
      "npy_url": "https://datjandra.github.io/breathflow/yang_jun.npy"
  },
  "Vive Health - Cat Cow Pose": {
      "video_url": "https://youtu.be/s3hc0UnFyio",
      "npy_url": "https://datjandra.github.io/breathflow/catcow.npy"
  },
  "Janice Tucker - Spinal Twist (Eight Brocades)": {
      "video_url": "https://youtu.be/fpQmwezSkrI",
      "npy_url": "https://datjandra.github.io/breathflow/wagtail.npy"
  }
}

def load_npy(url):
  response = requests.get(url)
  if response.status_code == 200:
      npy_file = io.BytesIO(response.content)
      reference_embeddings = np.load(npy_file, allow_pickle=True)
      return np.array(reference_embeddings.item().float)
  return None

def on_task_update(task: EmbeddingsTask, progress_bar, status_text, start_time):
  if task.status == "processing":
    # Increment the progress bar in steps, simulating progress
    status_text.text("Please wait, processing...")
    for i in range(0, 100, 5):
      time.sleep(0.5)  # Simulating time taken per update
      progress_bar.progress(i)
  elif task.status == "ready":
    progress_bar.progress(100)
    end_time = time.time()
    elapsed_time = round(end_time - start_time)  # Calculate total elapsed time   
    status_text.text(f"Completed in {elapsed_time} seconds")

def get_grade(cosine_similarity, threshold=0.5):
  # Map cosine similarity to letter grades and handle invalid cases.
  if cosine_similarity is None or np.isnan(cosine_similarity) or cosine_similarity < threshold:
      return None  # Invalid similarity or very low similarity case
  if cosine_similarity >= 0.9:
      return 'A'
  elif 0.8 <= cosine_similarity < 0.9:
      return 'B'
  elif 0.7 <= cosine_similarity < 0.8:
      return 'C'
  elif 0.6 <= cosine_similarity < 0.7:
      return 'D'
  else:
      return 'F'

def main():
  menu()
  st.title("Exercise Video Analysis")

  # Brief description and instructions
  st.write("""
  This tool allows you to analyze your exercise videos by comparing them with reference videos. 
  Based on the similarity between your movements and the reference video, a grade will be assigned.
  
  **Instructions:**
  1. Select an exercise video from the dropdown menu.
  2. Upload your own exercise video (MP4, MOV or MPEG4 format).
  3. Your video will be trimmed to the first few seconds for analysis.
  4. A grade will be assigned based on the similarity between your movements and the reference video.
  """)

  selected_option = st.selectbox("Select an exercise video", list(video_options.keys()))
  video_url = video_options[selected_option]["video_url"]
  npy_url = video_options[selected_option]["npy_url"]

  reference = load_npy(npy_url)
  st.header("Reference video")
  st.video(video_url)
  
  video_file = st.file_uploader("Please upload your video", type=['mp4', 'mov'])

  if video_file is not None:
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
  
    # Save the uploaded file to a temporary location
    video_path = os.path.join(temp_dir, video_file.name)
    with open(video_path, "wb") as f:
      f.write(video_file.read())

    # Load the video using moviepy
    clip = VideoFileClip(video_path)

    # Trim the video to cutoff seconds or less
    cutoff = 10
    duration = min(clip.duration, cutoff)  # Ensure it doesn't exceed cutoff seconds
    output_path = os.path.join(temp_dir, f"trimmed_{video_file.name}")
    ffmpeg_extract_subclip(video_path, 0, duration, targetname=output_path)

    # Display success message and the shortened video
    st.success(f"Video has been trimmed to {duration} seconds and saved.")
    st.video(output_path)

    client = TwelveLabs(api_key=TL_API_KEY)
    task = client.embed.task.create(
      engine_name="Marengo-retrieval-2.6",
      video_file=output_path,
      video_embedding_scopes=["video"]
    )

    # Create a progress bar for task updates
    progress_bar = st.progress(0)
    status_text = st.empty()
    start_time = time.time()
    
    status = task.wait_for_done(
      sleep_interval=2,
      callback=lambda t: on_task_update(t, progress_bar, status_text, start_time)
    )

    task_result = client.embed.task.retrieve(task.id)
    if task_result.video_embeddings is not None:
      for v in task_result.video_embeddings:
        student = np.array(v.embedding.float)
        cosine_similarity = np.dot(reference, student) / (norm(reference) * norm(student))
        grade = get_grade(cosine_similarity)
        if grade is None:
          st.error("The video is not a valid exercise video. Please upload a valid exercise video.")
        else:
          st.metric(label="Grade", value=grade)
    
if __name__ == "__main__":
  main()
