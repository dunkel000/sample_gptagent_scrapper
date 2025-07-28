FROM python:3.11-slim

# Install Selenium and BeautifulSoup. Chrome is not installed because the
# browser runs in a separate container managed by Docker Compose.
RUN pip install --no-cache-dir selenium==4.18.1 beautifulsoup4

# Copy the scraping script into the working directory
WORKDIR /app
COPY scraper.py /app/

# Default command: run the script
CMD ["python", "scraper.py"]