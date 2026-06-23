from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.linkedin.com/login")

    input("Login manually and press Enter...")

    context.storage_state(path="linkedin_state.json")

    browser.close()

print("Session saved successfully!")