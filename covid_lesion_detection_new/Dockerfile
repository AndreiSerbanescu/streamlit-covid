FROM nvidia/cuda:10.0-cudnn7-devel

WORKDIR /app

# Installing Python3 and Pip3
RUN apt-get update
RUN apt-get update && apt-get install -y python3-pip virtualenv
RUN pip3 install setuptools pip --upgrade --force-reinstall

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

#COPY files/source/code/covid /app/covidenv

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh \
    && echo PATH="/root/miniconda3/bin":$PATH >> .bashrc \
    && exec bash \
    && conda --version


#COPY files/source/code/requirements.txt /app/requirements.txt
COPY requirements-no-version-without-problematic-deps.txt /app/requirements.txt

RUN conda config --append channels conda-forge
RUN conda config --append channels simpleitk
RUN conda update --all


RUN conda create --name condaenv --file /app/requirements.txt

# Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "condaenv", "/bin/bash", "-c"]

COPY requirements-problematic-deps.txt /app/requirements-for-pip.txt
RUN pip install -r /app/requirements-for-pip.txt

RUN apt-get update
RUN apt-get install vim -y

#RUN pip3 install -r /app/requirements.txt
#
###############################

#RUN pip3 install cython==0.29.14
#RUN pip3 install h5py==2.10.0
#RUN pip3 install keras==2.2.4
#RUN pip3 install matplotlib==3.1.3
#RUN pip3 install numpy>=1.14
#RUN pip3 install opencv-python>=3.3.0
#RUN pip3 install pillow==7.0.0
#RUN pip3 install tqdm==4.40.2
#RUN pip3 install tensorflow-gpu==1.14.0
#RUN pip3 install simpleitk==1.2.4




COPY covid /app/covidenv
COPY files/source/code/ /app/code
COPY files/source/model /app/model

# TODO make alias python work as to not change setup-env script
RUN cd /app/code && sh setup-env.sh

## fix opencv import issue
RUN apt-get install libsm6 libxext6 libxrender-dev -y

# fix opencv import issue
RUN apt install libgl1-mesa-glx -y


RUN mkdir /app/data_share
ENV DATA_SHARE_PATH /app/data_share

COPY files/interface/ /app/

ENV LD_LIBRARY_PATH /usr/local/cuda-10.0:/usr/local/nvidia/lib:/usr/local/nvidia/lib64
