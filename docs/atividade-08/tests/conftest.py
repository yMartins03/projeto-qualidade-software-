import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
        page.evaluate("""
            () => {
                localStorage.setItem('userId', '1');
                localStorage.setItem('userName', 'Teste Automação BDD');
            }
        """)
        
        yield page
        browser.close()


@pytest.fixture
def base_url():
    return "https://local-eats-unisenac.vercel.app/static/index.html"
