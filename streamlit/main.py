import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
from PIL import Image

lung = Image.open("lung.png").resize((500, 500))
seg = Image.open("seg.png").resize((500, 500))


#### Page Header #####
# st.title("CoCaCoLA - The Cool Calculator for Corona Lung Assessment")
st.title("CoViD-19 Risk Calculator")  # for more formal occasions :S
pcr_positive = st.checkbox("PCR Positive?")
#### Page Header #####

##### Sidebar ######
st.sidebar.title("Clinical Data")
st.sidebar.subheader("Basic Data")
sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
age = st.sidebar.number_input("Age", min_value=0, max_value=110, step=1, value=50)
weight = st.sidebar.number_input("Weight", min_value=0, max_value=150, step=1, value=70)
height = st.sidebar.number_input(
    "Height", min_value=120, max_value=200, step=1, value=160
)
st.sidebar.subheader("Pre-existing Conditions")
diabetes = st.sidebar.checkbox("Diabetes")
smoking = st.sidebar.checkbox("Smoking")
emphysema = st.sidebar.checkbox("Pulmonary Disease")
stroke = st.sidebar.checkbox("Previous Stroke")
cardiac = st.sidebar.checkbox("Cardiac Disease")
oncologic = st.sidebar.checkbox("Cancer")
immuno = st.sidebar.checkbox("Immunodeficiency or Immunosuppression")

st.sidebar.subheader("Laboratory")
lymphos = st.sidebar.selectbox("Lymphocytes", ("Lowered", "Normal", "Elevated"))
crp = st.sidebar.number_input("CRP", min_value=0.0, max_value=50.0, step=0.1, value=0.5)
crea = st.sidebar.number_input(
    "Creatinine", min_value=0.0, max_value=5.0, step=0.1, value=1.0
)
dimers = st.sidebar.number_input(
    "D-Dimers", min_value=0, max_value=5000, step=100, value=500
)
ldh = st.sidebar.number_input("LDH", min_value=0, max_value=5000, step=10, value=240)
##### Sidebar ######


##### File Selector #####
st.header("Please Upload the Chest CT DICOM here")
st.file_uploader(label="", type=["dcm", "dicom"])
##### File Selector #####


##### Output Area #####
st.header("Result:")
st.subheader("Probability of Covid-19 infection=96.5%")
st.subheader("Covid-19 severity index: 1")

##### Output Area #####
st.image([lung, seg])
