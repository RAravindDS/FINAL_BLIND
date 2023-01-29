import os 
import shutil 
# import gdown 
import tempfile 
import os 
import base64
import streamlit as st 


print('fine')
st.header("Prediction Tab")
st.markdown("""
    <center><h1>Welcome to Blind Navigation System Project!</h1></center><body>
    <li>This project is built based on <b>MLOPS maturity level 3</b>. </li>
    <li>This includes <b>github actions</b>, <b>docker</b>, <b>CI/ CD (continous delivery and 
          continuous deployment)</b> and <b>K8's</b> (to auto scale)!</li>
    <li> This is basically a <b>object detection model</b>( <b>yolo v8</b>) with the <b>distance estimation</b>.</li>
    <li>I basically built the app if any object near to 5 meter, it will provide the audio signal to user with the object name and distance of the object!</li>
    <li>Basically I got the repo from here <a href="https://github.com/HassanBinHaroon/object_detection-PLUS-distance_estimation-v1">GitHub</a>. I just implemented with some modification! </li>
    <li>I have tried some other apporaches but I not able to figure it out!</li></body>""")

file = st.file_uploader("Choose a video...", type=["mp4"])
if st.button('submit'):
    with st.spinner("Inferene going on.."): 
        with open("videos/uploaded_video.mp4", "wb") as f:
            f.write(file.read())

        path="object-detector/results/"
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
            print("Directory Deleted!")
        video_link = "../videos/uploaded_video.mp4"
        output_file_name = "walking_output_output.mp4"
        os.chdir("object-detector")
        os.system(f"python detect.py --save-txt --weights training-results/weights/best.pt --conf 0.4 --source {video_link}")
        os.chdir("..")
        os.chdir("distance-estimator")
        os.system("python inference.py --data ../object-detector/results/data/data.csv --model models/model@1535470106.json --weights models/model@1535470106.h5 --results .")
        os.system(f"python visualizer.py --data predictions.csv --frames ../object-detector/results/frames/ -fps 90 --results . -p {output_file_name} ") 

        os.chdir("../object-detector/results/frames/")
        video_file = open('output.mp4', 'rb')
        
        video_bytes = video_file.read()
        st.video(video_bytes)
        
        st.write("If the video is not visible download it!")
        video_base64 = base64.b64encode(open('output.mp4', "rb").read()).decode()
        st.markdown(f'<a href="data:video/mp4;base64,{video_base64}" download="video.mp4">Download Video</a>', unsafe_allow_html=True)
        