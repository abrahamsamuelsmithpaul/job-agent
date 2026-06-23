from playwright.sync_api import sync_playwright

print("Step 1")

with sync_playwright() as p:
    print("Step 2")

    browser = p.chromium.launch(headless=False)

    print("Step 3")

    page = browser.new_page()

    print("Step 4")

    page.goto("https://www.google.com")

    print("Step 5")

    page.wait_for_timeout(5000)

    browser.close()

print("Step 6")