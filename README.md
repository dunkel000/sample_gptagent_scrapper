# sample_gptagent_scrapper

This repository contains a sample scraper that runs in Docker containers using
Selenium and Docker Compose. The `browser` service starts a Chrome instance with
its remote WebDriver and a noVNC server so you can monitor the browsing
session, while the `scraper` service runs a Python script that connects to the
browser and extracts data.

## Structure

- `Dockerfile` – Image that contains Python, Selenium and the scraping script.
- `docker-compose.yml` – Defines the `browser` and `scraper` services.
- `scraper.py` – Python code that connects to the remote browser and performs
  the scraping.

## Usage

1. Build the images and start the services interactively:

   ```bash
   docker‑compose up --build
   ```

2. Open your browser at `http://localhost:7900` and enter the password
   `secret` to access the noVNC interface and see what happens in Chrome.

3. The `scraper.py` script will run automatically when the `scraper` container
   starts and will print the title of the target page. Modify `scraper.py` to
   suit your needs.

## Notes

- Port 4444 exposed by the `browser` container is the remote WebDriver where
  Selenium connects. Port 7900 exposes the noVNC web interface so you can see
  and interact with the browser.
- This example uses `seleniarm/standalone-chromium:latest`, but you can replace
  it with `selenium/standalone-firefox` or `selenium/standalone-edge` depending
  on your needs.