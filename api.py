import logging
import os
from flask import Flask, request, jsonify
import requests

# === Logging pour debug payload ===
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# URL de votre micro-service pricer en ligne (à configurer via variable d'env)
PRICER_PRICE_URL = os.environ.get("PRICER_PRICE_URL")

# Validation des modèles et produits
VALID_MODELS = {"Heston", "Bates", "Double Heston"}
VALID_PRODUCTS = {
    "Cash-or-Nothing Call", "Cash-or-Nothing Put",
    "Asset-or-Nothing Call", "Asset-or-Nothing Put",
    "Gap Option Call", "Gap Option Put",
    "Super Share Option Call", "Super Share Option Put",
    "One-Touch Option", "No-Touch Option",
    "Double One-Touch Option", "Double No-Touch Option",
    "Ladder Option Call", "Ladder Option Put",
    "Range Binary Option", "Range Reverse Binary Option",
    "Up-and-In Binary", "Down-and-In Binary",
    "Classic Variance Swap", "Floating Strike Variance Swap",
    "Log Contract Variance Swap", "Volatility Swap",
    "Gamma Swap", "Conditional Variance Swap"
}

@app.route('/parameter', methods=['