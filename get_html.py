from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


def find_images():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    with sync_playwright() as file:

        # Open Browser
        browser = file.chromium.launch(headless=True)
        page = browser.new_page()

        # Set user agent
        context = browser.new_context(user_agent=user_agent)
        page = context.new_page()

        # Go to page and wait to load
        page.goto("https://www.pexels.com/search/cat/")
        page.wait_for_load_state("networkidle", timeout=90000)
        print("Got Load State")

        # Wait for specific selector to show up 
        page.wait_for_selector("article[class *= 'MediaCard'] > a > img")
        print("Selector Found")

        # Get and parse required html
        html = page.inner_html("body")
        tree = HTMLParser(html)
        divs = tree.css("article[class *= 'MediaCard'] > a > img")
    
    return divs