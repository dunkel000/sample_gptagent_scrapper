FROM python:3.11-slim

# Instala Selenium y BeautifulSoup.  No instalamos Chrome porque el navegador
# se ejecuta en un contenedor separado gestionado por Docker Compose.
RUN pip install --no-cache-dir selenium==4.18.1 beautifulsoup4

# Copia el script de scraping al directorio de trabajo
WORKDIR /app
COPY scraper.py /app/

# Comando por defecto: ejecuta el script
CMD ["python", "scraper.py"]