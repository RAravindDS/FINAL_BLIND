FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 8501
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python first.py 
RUN cd Blind/navigaion_System/object_detection-PLUS-distance_estimation-v1/
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]