import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻")
st.markdown(
    """
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .title {
            color: #4b4bff;
            font-size: 36px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title">💻 Laptop Price Predictor 💰</p>', unsafe_allow_html=True)

# UI Inputs
company = st.selectbox('Brand', df['Company'].unique())
type_ = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight of the Laptop (in Kg)')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Display', ['No', 'Yes'])

screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.3)
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080', '1366x768', '1600x900', '3840x2160',
     '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
)

cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
os = st.selectbox('Operating System', df['os'].unique())

# Predict button
if st.button('Predict Price'):
    # Binary encoding
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # PPI calculation
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    # DataFrame for prediction
    query = pd.DataFrame(
        [[company, type_, ram, weight, touchscreen, ips, ppi,
          cpu, hdd, ssd, gpu, os]],
        columns=[
            'Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen',
            'Ips', 'PPI', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'
        ]
    )

    # Type casting to avoid model input issues
    query = query.astype({
        'Company': str,
        'TypeName': str,
        'Ram': np.int32,
        'Weight': np.float32,
        'Touchscreen': np.int32,
        'Ips': np.int32,
        'PPI': np.float32,
        'Cpu brand': str,
        'HDD': np.int32,
        'SSD': np.int32,
        'Gpu brand': str,
        'os': str
    })

    # Model prediction (price was log-transformed during training)
    predicted_log_price = pipe.predict(query)[0]
    predicted_price = int(np.exp(predicted_log_price))

    # Output
    st.success(f"💸 The predicted price of this laptop configuration is ₹{predicted_price}")
