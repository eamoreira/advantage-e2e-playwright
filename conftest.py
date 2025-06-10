import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """
    Fixture do Playwright configurada para o projeto
    Configurações escolhidas depois de alguns ajustes para estabilidade
    """
    with sync_playwright() as p:
        # headless=False para ver o que está acontecendo durante desenvolvimento
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720}  # Viewport fixo evita problemas
        )
        page = context.new_page()
        page.set_default_timeout(60000)  # 60 segundos - site às vezes é lento
        yield page
        page.close()
        context.close()
        browser.close()