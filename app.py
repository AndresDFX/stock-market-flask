"""Servicio web del Taller 1: expone por HTTP los datos de un stock y su valor promedio."""
import os
from datetime import datetime

from flask import Flask, jsonify, request

import read_value_yf

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Lo mismo que el taller: la tabla de GOOGL desde 2020 en HTML."""
    return read_value_yf.test().to_html()


@app.route("/stock/<ticker>")
def stock(ticker):
    """Promedio de cierre de un ticker entre ?inicio=YYYY-MM-DD y ?fin=YYYY-MM-DD."""
    inicio = request.args.get("inicio", "2020-01-01")
    fin = request.args.get("fin")
    data = read_value_yf.get_stock_data(inicio, ticker.upper(), fin)
    if data.empty:
        return jsonify(error=f"Sin datos para {ticker} en ese periodo"), 404
    return jsonify(ticker=ticker.upper(), inicio=inicio, fin=fin or str(datetime.now().date()), dias=len(data),
                   promedio_cierre=round(read_value_yf.promedio_cierre(data), 2))


@app.route("/health")
def health():
    return jsonify(status="ok", hora=datetime.now().isoformat(timespec="seconds"))


if __name__ == "__main__":
    print(f"{datetime.now()}")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
