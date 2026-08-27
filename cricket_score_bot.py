from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page(
        viewport={"width": 1280, "height": 900}
    )

    # Cricbuzz
    page.goto("https://www.cricbuzz.com/", wait_until="domcontentloaded")

    # Wait for page to load
    page.wait_for_timeout(5000)

    # Screenshot of Cricbuzz homepage
    page.screenshot(
        path="cricbuzz_score.png",
        full_page=True
    )

    print("Screenshot saved as cricbuzz_score.png")

    browser.close()
