from playwright.sync_api import sync_playwright
import smtplib
import time
from selectolax.parser import HTMLParser

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

with sync_playwright() as file:
    browser = file.chromium.launch(headless=True)
    page = browser.new_page()
    context = browser.new_context(user_agent=user_agent)
    page = context.new_page()

    page.goto("https://www.pexels.com/search/cat/")
    page.wait_for_load_state("networkidle", timeout=90000)
    print("Got Load State")

    page.wait_for_selector("article[class *= 'MediaCard'] > a > img")
    print("Selector Found")

    html = page.inner_html("body")
    tree = HTMLParser(html)
    divs = tree.css("article[class *= 'MediaCard'] > a > img")

