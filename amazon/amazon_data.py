# from bs4 import BeautifulSoup
# import requests
#
# root = "https://www.amazon.in/"
# website = f"{root}/s?k=lenovo+laptop&crid=3TJQB0G2OW73Z&sprefix=lenova%2Caps%2C355&ref=nb_sb_ss_mvt-t11-ranker_3_6"
# result = requests.get(website)
# content = result.text
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/139.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9"
# }
#
# response= requests.get(website, headers=headers)
# soup = BeautifulSoup(response.text, "lxml")
#
# box = soup.find_all("div", class_="a-section a-spacing-small a-spacing-top-small")
#
# for boxes in box:
#     title = boxes.get()
#     price_tag = box.find("span", class_="a-price-whole")
#     price = price_tag.get_text(strip=True) if price_tag else "Price not available"
#
#     print(f"Title: {title}")
#     print(f"Price: ₹{price}")
#     print("-" * 50)


import requests
from bs4 import BeautifulSoup

# Amazon search URL for Lenovo laptops
url = "https://www.amazon.in/s?k=lenovo+laptop"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0.0.0 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product boxes
box = soup.find_all("div", class_="a-section")

for item in box:
    # Get the title
    title = item.find("h2")

    # Get the price
    price = item.find("span", class_="a-price-whole")
    price = price.get_text(strip=True) if price else "Not Available"

    print(title)
    print(price)
    print("-" * 50)
