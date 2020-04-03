FROM nvidia/cuda:latest

WORKDIR /app

# Installing Python3 and Pip3
RUN apt-get update
RUN apt-get update && apt-get install -y python python-dev python3.7 python3.7-dev python3-pip virtualenv libssl-dev libpq-dev git build-essential libfontconfig1 libfontconfig1-dev
RUN pip3 install setuptools pip --upgrade --force-reinstall

# Installing lungmask

# this is for avoiding Unicode decode error for the pip3 command
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
RUN apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    pip3 install git+https://github.com/JoHof/lungmask

# Loading all three Unet models - R231, LTRCLobes and R231CovidWeb
COPY load_models.py /app/
RUN python3 /app/load_models.py

RUN pip3 install streamlit
RUN pip3 install sklearn
RUN pip3 install xnat
RUN pip3 install dicom2nifti

COPY start.py /app/main.py
COPY main.py /app/main.py
COPY lung.png /app/lung.png
COPY seg.png /app/seg.png
