FROM python:3.11-slim
WORKDIR /work
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=5000
EXPOSE 5000
# gunicorn en vez del servidor de desarrollo de Flask: es lo adecuado en la nube
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} -w 2 --timeout 120 app:app"]
