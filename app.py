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
        "maturities_values": [1/12, 2/12, 3/12, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 7, 10],
        "strikes_pct": ["80% - 1663.95","90% - 1871.95","95% - 1975.94","97.5% - 2027.94","100% - 2079.94","102.5% - 2131.94","105% - 2183.94","110% - 2287.93","120% - 2495.93"],
        "strikes_values": [0.8, 0.9, 0.95, 0.975, 1.0, 1.025, 1.05, 1.1, 1.2]
    },
    "SPX Index 2014": {
        "metadata": {
            "underlying":    "SPX 2014",
            "date":          "09/06/2014",
            "dividend_rate": 2.26,
            "spot_price":    1951.16,
            "interest_rate": 1.40
        },
        "maturities":  ["1M","2M","3M","6M","9M","1Y","18M","2Y","3Y","4Y","5Y","7Y","10Y"],
        "maturities_values": [1/12, 2/12, 3/12, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 7, 10],
        "strikes_pct": ["80% - 1560.93","90% - 1756.04","95% - 1853.60","97.5% - 1902.38","100% - 1951.16","102.5% - 1999.94","105% - 2048.72","110% - 2146.28","120% - 2341.39"],
        "strikes_values": [0.8, 0.9, 0.95, 0.975, 1.0, 1.025, 1.05, 1.1, 1.2]
    }
}

models = ["Heston", "Bates", "Double Heston"]
products = [
    "Cash-or-Nothing Call", "Cash-or-Nothing Put", "Asset-or-Nothing Call", "Asset-or-Nothing Put", "Gap Option Call", "Gap Option Put",
    "Super Share Option Call", "Super Share Option Put", "One-Touch Option", "No-Touch Option", "Double One-Touch Option", "Double No-Touch Option",
    "Ladder Option Call", "Ladder Option Put", "Range Binary Option", "Range Reverse Binary Option", "Up-and-In Binary", "Down-and-In Binary", "Classic Variance Swap", 
    "Floating Strike Variance Swap", "Log Contract Variance Swap", "Volatility Swap", "Gamma Swap", "Conditional Variance Swap"
]

def price_option(inputs: dict) -> float:
    """Stub de pricing – remplacer par le vrai moteur."""
    time.sleep(1)  # simuler un calcul
    return 42.0

# 4) Titre principal
st.markdown('<div class="main-header">🔧 Options Pricing Tool</div>', unsafe_allow_html=True)

# 5) Sidebar pour les sélections
with st.sidebar:
    st.header("🗂️ Parameters selection")
    matrix = st.selectbox("1) Underlying asset", list(vol_matrices.keys()))
    maturity = st.selectbox("2) Maturity (years)", vol_matrices[matrix]["maturities"])
    strike_pct = st.selectbox("3) Strike (% of spot) and strike price", vol_matrices[matrix]["strikes_pct"])
    
    model = st.selectbox("4) Pricing model", models)
    product = st.selectbox("5) Type of derivative product", products)
    do_price = st.button("Request a price quote")

# 6) Construire le dict d'inputs
meta = vol_matrices[matrix]["metadata"]
index_maturity = vol_matrices[matrix]["maturities"].index(maturity)
index_strike = vol_matrices[matrix]["strikes_pct"].index(strike_pct)

inputs = {
    "matrix":        matrix,
    "maturity":      vol_matrices[matrix]["maturities_values"][index_maturity],
    "strike_pct":    vol_matrices[matrix]["strikes_values"][index_strike],
    "model":         model,
    "product":       product,
    "underlying":    meta["underlying"],
    "date":          meta["date"],
    "dividend_rate": meta["dividend_rate"],
    "spot_price":    meta["spot_price"],
    "interest_rate": meta["interest_rate"]
}

# 7) Pricing & affichage
if do_price:
    with st.spinner("🔄 Calibration & pricing in progress…"):
        price = price_option(inputs)

    # 7.1) Prix en grand
    st.markdown("## 💰 Option Price quote Bid Ask")
    c1, _ = st.columns([1, 3])
    c1.markdown(
        f"<h1 style='color:#1F77B4; font-size:3rem; margin:0;'>{price:.4f}</h1>",
        unsafe_allow_html=True
    )

    # 7.2) Metrics metadata
    st.markdown("### 📋 Parameters used as Volatility matrix")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Underlying",      inputs["underlying"])
    m2.metric("Date",            inputs["date"])
    m3.metric("Dividend Rate %", f"{inputs['dividend_rate']:.2f}%")
    m4.metric("Spot Price",      f"{inputs['spot_price']:.2f}")
    m5.metric("Interest Rate %", f"{inputs['interest_rate']:.2f}%")

    # 7.3) Tableau récapitulatif
    st.markdown("### ⚙️ Choosen parameter recap")
    st.table({
        "Parameter": [
            "Underlying", "Maturity (years)", "Strike (% spot) and strike price",
            "Model used", "Financial product"
        ],
        "Value": [
            inputs["matrix"],
            f"{maturity} ({inputs['maturity']} ans)",
            f"{strike_pct} ({inputs['strike_pct'] * 100:.2f}%)",
            inputs["model"],
            inputs["product"]
        ]
    })
