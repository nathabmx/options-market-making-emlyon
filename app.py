import streamlit as st
import time

# 1) Configuration de la page
st.set_page_config(page_title="  Options Pricing Tool", layout="wide")

# 2) CSS pour un rendu soigné
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        color: #1F77B4;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #1F77B4;
        color: #fff;
        border-radius: 0.5rem;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3) Données de base avec maturities et strikes modifiés
vol_matrices = {
    "NASDAQ 100 Index 2015": {
        "metadata": {
            "underlying":    "NASDAQ 2015",
            "date":          "09/06/2015",
            "dividend_rate": 1.32,
            "spot_price":    1004427.61,
            "interest_rate": 1.50
        },
        "maturities":  ["1M","2M","3M","6M","9M","1Y","18M","2Y","3Y","4Y","5Y","7Y","10Y"],
        "maturities_values": [1/12, 2/12, 3/12, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 7, 10],
        "strikes_pct": ["80% - 3542.09","90% - 3984.85","95% - 4206.23","97.5% - 4316.92","100% - 4427.61","102.5% - 4538.30","105% - 4648.99","110% - 4870.37","120% - 5313.13"],
        "strikes_values": [0.8, 0.9, 0.95, 0.975, 1.0, 1.025, 1.05, 1.1, 1.2]
    },
    "NASDAQ 100 Index 2014": {
        "metadata": {
            "underlying":    "NASDAQ 2014",
            "date":          "09/06/2014",
            "dividend_rate": 1.50,
            "spot_price":    3795.74,
            "interest_rate": 1.40
        },
        "maturities":  ["1M","2M","3M","6M","9M","1Y","18M","2Y","3Y","4Y","5Y","7Y","10Y"],
        "maturities_values": [1/12, 2/12, 3/12, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 7, 10],
        "strikes_pct": ["80% - 3036.59","90% - 3416.17","95% - 3605.95","97.5% - 3700.85","100% - 3795.74","102.5% - 3890.63","105% - 3985.53","110% - 4175.31","120% - 4554.89"],
        "strikes_values": [0.8, 0.9, 0.95, 0.975, 1.0, 1.025, 1.05, 1.1, 1.2]
    },
    "SPX Index 2015": {
        "metadata": {
            "underlying":    "SPX 2015",
            "date":          "09/06/2015",
            "dividend_rate": 2.15,
            "spot_price":    2079.94,
            "interest_rate": 1.5
        },
        "maturities":  ["1M","2M","3M","6M","9M","1Y","18M","2Y","3Y","4Y","5Y","7Y","10Y"],
        "maturities_values": [1/12