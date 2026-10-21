# Stock Market como servicio web

Taller 1 de Computación Distribuida y Frameworks para Desarrollo de Aplicaciones Inteligentes (Univalle).
Es un web service en Python con Flask que consulta Yahoo Finance con `yfinance`. Va empaquetado en Docker y desplegado en Render.

## Endpoints

| Ruta | Qué devuelve |
|---|---|
| `/` | Tabla HTML con los precios de GOOGL desde 2020 (el ejemplo del taller) |
| `/stock/<ticker>?inicio=YYYY-MM-DD&fin=YYYY-MM-DD` | JSON con el valor promedio de cierre del stock en el periodo |
| `/health` | Estado del servicio |

## Correrlo con Docker

```bash
docker image build -t stock-market:2.0 .
docker container run --rm -p 5000:5000 stock-market:2.0
# http://localhost:5000/stock/AMZN?inicio=2024-01-01&fin=2024-06-30
```

`read_value_yf.py` también corre solo, como en la primera parte del taller: `python read_value_yf.py AMZN`.
