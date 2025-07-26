# sample_gptagent_scrapper

Este repositorio contiene un ejemplo de «scraper» que se ejecuta en contenedores
Docker utilizando Selenium y Docker Compose.  El servicio `browser` levanta una
instancia de Chrome con su WebDriver remoto y un servidor noVNC para poder
monitorear la navegación, mientras que el servicio `scraper` ejecuta un
script Python que se conecta al navegador y extrae datos.

## Estructura

- `Dockerfile` – Imagen que contiene Python, Selenium y el script de scraping.
- `docker-compose.yml` – Define los servicios `browser` y `scraper`.
- `scraper.py` – Código Python que se conecta al navegador remoto y realiza el
  scraping.

## Uso

1. Construye las imágenes y arranca los servicios en modo interactivo:

   ```bash
   docker‑compose up --build
   ```

2. Abre tu navegador en `http://localhost:7900` e introduce la contraseña
   `secret` para acceder a la interfaz noVNC y ver lo que sucede en Chrome.

3. El script `scraper.py` se ejecutará automáticamente al arrancar el
   contenedor `scraper` y mostrará el título de la página objetivo.  Puedes
   modificar `scraper.py` para adaptarlo a tus necesidades.

## Notas

- El puerto 4444 expuesto por el contenedor `browser` es el WebDriver remoto
  donde se conecta Selenium.  El puerto 7900 expone la interfaz web noVNC que
  te permite ver e interactuar con el navegador.
- Este ejemplo utiliza `selenium/standalone-chrome:latest`, pero puedes
  reemplazarlo por `selenium/standalone-firefox` o `selenium/standalone-edge`
  según tus necesidades.