import ssl
import os
from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve

ssl._create_default_https_context = ssl._create_unverified_context

pw = sync_playwright().start()
# os.makedirs("pdf_data", exist_ok=True)

browser = pw.chromium.launch(
    # headless=False,
    slow_mo=2000
)
page = browser.new_page()
page.goto('https://arxiv.org/search/')
page.get_by_placeholder('Search term...').fill('neural Network')
page.get_by_role('button').nth(1).get_by_text('Search').click()

# get all abstract links instead
links = page.locator("xpath=//a[contains(@href, 'arxiv.org/pdf')]").all()

for link in links:
    url = link.get_attribute('href')
    # print(url)
    urlretrieve(url, "pdf/" + url[-1:] + ".pdf")
browser.close()




