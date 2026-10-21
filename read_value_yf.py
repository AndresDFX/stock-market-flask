"""Datos de un stock entre dos fechas con yfinance (Taller 1, Computación Distribuida y Frameworks)."""
import sys
from datetime import date

import yfinance as yf


def get_stock_data(sd, stock, ed=None):
    """DataFrame de pandas con los precios de `stock` entre `sd` y `ed` (por defecto, hoy). Fechas en YYYY-MM-DD."""
    return yf.download(stock, sd, ed or date.today().isoformat(), progress=False, auto_adjust=False)


def promedio_cierre(data):
    """Valor promedio del precio de cierre en el periodo: lo que pide el escenario del taller."""
    return float(data["Close"].mean().iloc[0] if hasattr(data["Close"].mean(), "iloc") else data["Close"].mean())


def test(ticker="GOOGL"):
    return get_stock_data("2020-01-01", ticker)


if __name__ == "__main__":
    ticker = sys.argv[1] if len(sys.argv) == 2 else "GOOGL"
    print(f"Se recuperara informacion del stock ${ticker}")
    data = test(ticker)
    print(data.tail())
    print(f"Promedio de cierre: {promedio_cierre(data):.2f}")
