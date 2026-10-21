# Stock Market como servicio web

Taller 1 de Computación Distribuida y Frameworks para Desarrollo de Aplicaciones Inteligentes (Univalle).
Es un web service en Python con Flask que consulta Yahoo Finance con `yfinance`. Va empaquetado en Docker y desplegado en Render.

**Servicio en la nube:** https://stock-market-flask.onrender.com

El plan es gratuito: si el servicio estuvo inactivo, la primera petición tarda unos segundos mientras el contenedor arranca.

## Endpoints

| Ruta | Qué devuelve |
|---|---|
| [`/`](https://stock-market-flask.onrender.com/) | Tabla HTML con los precios de GOOGL desde 2020 (el ejemplo del taller) |
| [`/stock/<ticker>?inicio=YYYY-MM-DD&fin=YYYY-MM-DD`](https://stock-market-flask.onrender.com/stock/GOOGL?inicio=2020-01-01&fin=2022-01-01) | JSON con el valor promedio de cierre del stock en el periodo |
| [`/health`](https://stock-market-flask.onrender.com/health) | Estado del servicio |

## Del script al servicio, como en la guía del taller

| Paso | Archivo | Imagen |
|---|---|---|
| El script, por línea de comandos | `read_value_yf.py` | `stock-market:1.0`, con `Dockerfile.cli` |
| El servicio web con Flask | `app.py` | `stock-market:2.0`, con `Dockerfile` |

```bash
# 1.0: el script dentro de un contenedor; el stock se elige con la variable STOCK
docker image build -t stock-market:1.0 -f Dockerfile.cli .
docker container run --rm stock-market:1.0
docker container run --rm -e STOCK=AMZN stock-market:1.0

# 2.0: el servicio web
docker image build -t stock-market:2.0 .
docker container run --rm --name stock-market -p 5000:5000 stock-market:2.0
# http://localhost:5000/stock/AMZN?inicio=2024-01-01&fin=2024-06-30
```

`read_value_yf.py` también corre sin Docker: `python read_value_yf.py AMZN`.

## Despliegue en Render

- Es un servicio web de tipo Docker creado desde este repositorio. Render construye la imagen con `Dockerfile` en cada push a `main`.
- Corre en la región de Virginia (EE. UU.), en el plan gratuito, con verificación de salud en `/health`.
- Render asigna el puerto en la variable `PORT`. El `Dockerfile` arranca gunicorn en ese puerto, o en el 5000 si no está definida.

## Dos diferencias con la guía

- **gunicorn en vez de `python3 app.py`.** El servidor que trae Flask es de desarrollo; en la nube conviene un servidor WSGI.
- **`yfinance` reciente con `curl_cffi`.** Yahoo bloquea las peticiones simples que salen de las IP de los proveedores de nube, y desde Render el servicio no recibía datos. Con `yfinance` 0.2.58 o posterior y `curl_cffi`, las peticiones se presentan como las de un navegador y Yahoo las responde.

## Publicar la imagen en Docker Hub

Este paso de la guía es opcional:

```bash
docker image tag stock-market:2.0 <usuario>/stock-market:2.0
docker login
docker image push <usuario>/stock-market:2.0
```
