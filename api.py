import logging
import os
from flask import Flask, request, jsonify
import requests

# === Logging pour debug payload ===
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# 0) Health check endpoint
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# 1) URL de votre micro-service pricer en ligne (via variable d'environnement)
PRICER_PRICE_URL = os.environ.get("PRICER_PRICE_URL")

# 2) Validation des modèles et produits
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

# 3) Endpoint principal
@app.route('/parameter', methods=['POST'])
def parameter():
    data = request.get_json() or {}
    app.logger.info(f"🔥 Payload reçu sur /parameter : {data}")

    # 3.1) Vérification configuration du pricer
    if not PRICER_PRICE_URL:
        return jsonify({"error": "Service pricer non configuré."}), 503

    # 3.2) Extraction des champs requis
    model = data.get("model")
    product = data.get("product")
    strike = data.get("strike")
    maturity = data.get("maturity")

    # 3.3) Validation des champs
    if not model or not product or strike is None or maturity is None:
        return jsonify({"error": "Champs manquants : model, product, strike, maturity sont requis."}), 400
    if model not in VALID_MODELS:
        return jsonify({"error": f"Modèle '{model}' non supporté."}), 400
    if product not in VALID_PRODUCTS:
        return jsonify({"error": f"Produit '{product}' non supporté."}), 400

    # 3.4) Forward to pricer
    payload = {"model": model, "product": product, "strike": strike, "maturity": maturity}
    try:
        resp = requests.post(PRICER_PRICE_URL, json=payload, timeout=10)
        resp.raise_for_status()
        result = resp.json()
    except requests.RequestException:
        return jsonify({"error": "Service pricer indisponible."}), 502
    except ValueError:
        return jsonify({"error": "Réponse du pricer invalide (JSON attendu)."}), 502

    price = result.get("price")
    if price is None:
        return jsonify({"error": "Clé 'price' absente de la réponse du pricer."}), 502
    return jsonify({"price": price}), 200

# 4) Entry point
if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5001'))
    app.run(host='0.0.0.0', port=port)





