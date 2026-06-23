from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from datetime import datetime
import os

# Load environment variables
load_dotenv()

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

if not EMAIL or not PASSWORD:
    raise ValueError(
        "NAUKRI_EMAIL and NAUKRI_PASSWORD must be set in .env"
    )


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        try:
            print("Opening Naukri...")

            page.goto(
                "https://www.naukri.com/",
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(5000)

            os.makedirs("logs", exist_ok=True)

            # Debug screenshot
            page.screenshot(
                path="logs/homepage.png"
            )

            print("Clicking Login...")

            page.locator("text=Login").first.click()

            page.wait_for_timeout(3000)

            print("Entering credentials...")

            page.get_by_role(
                "textbox",
                name="Enter your active Email ID /"
            ).fill(EMAIL)

            page.get_by_role(
                "textbox",
                name="Enter your password"
            ).fill(PASSWORD)

            page.get_by_role(
                "button",
                name="Login",
                exact=True
            ).click()

            print("Waiting for login...")

            page.wait_for_timeout(8000)

            page.screenshot(
                path="logs/after_login.png"
            )

            print("Opening profile...")

            page.get_by_role(
                "link",
                name="View profile"
            ).click()

            page.wait_for_timeout(5000)

            page.screenshot(
                path="logs/profile_page.png"
            )

            print("Opening edit screen...")

            page.get_by_role(
                "emphasis"
            ).first.click()

            page.wait_for_timeout(3000)

            print("Saving profile...")

            page.get_by_role(
                "button",
                name="Save"
            ).click()

            page.wait_for_timeout(5000)

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            page.screenshot(
                path=f"logs/naukri_refresh_{timestamp}.png",
                full_page=True
            )

            print(
                f"SUCCESS: logs/naukri_refresh_{timestamp}.png"
            )

        except Exception as e:
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            page.screenshot(
                path=f"logs/error_{timestamp}.png",
                full_page=True
            )

            print(f"ERROR: {e}")

            raise

        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    run()