import os
from selenium import webdriver
from bs4 import BeautifulSoup


def get_driver() -> webdriver.Remote:
    """
    Crea y devuelve una instancia de WebDriver que se conecta al navegador
    remoto especificado por la variable de entorno `BROWSER_URL`.  Utiliza
    opciones recomendadas para entornos Docker.
    """
    browser_url = os.environ.get("BROWSER_URL", "http://localhost:4444/wd/hub")
    options = webdriver.ChromeOptions()
    # Reduce el uso de memoria compartida dentro de contenedores
    options.add_argument("--disable-dev-shm-usage")
    # No se añade --headless para poder observar la navegación via noVNC
    return webdriver.Remote(command_executor=browser_url, options=options)


def main():
    # Página de ejemplo.  Cámbiala por la URL que quieres scrapear.
    url = "https://example.com"
    driver = get_driver()
    try:
        driver.get(url)
        # Extrae el HTML generado tras la carga completa de la página
        soup = BeautifulSoup(driver.page_source, "html.parser")
        print("Título de la página:", soup.title.get_text() if soup.title else "(sin título)")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()