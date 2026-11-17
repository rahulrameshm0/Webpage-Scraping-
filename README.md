# Webpage Scraping

A collection of hands-on web scraping projects built while learning to extract data from real websites. The repo covers static HTML parsing, pagination, AJAX/JavaScript-rendered pages, hidden JSON APIs, form/login flows, and file downloads — using **Scrapy**, **Beautiful Soup**, **Playwright**, and **requests**.

> ⚠️ **Educational use only.** These scrapers were written to practise scraping techniques against public/demo sites. Always check a site's `robots.txt` and Terms of Service before scraping, respect rate limits, and never commit live session cookies or tokens (the ones in this repo are expired).

---

## Tech stack

| Tool | Used for |
| --- | --- |
| [Scrapy](https://scrapy.org/) | Most spiders: crawling, pagination, items, pipelines |
| [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) + requests | Simple static-page scraping |
| [Playwright](https://playwright.dev/python/) | JavaScript-rendered listings and PDF downloads |
| pandas | Saving hidden-API results to Excel/CSV |

---

## Projects

### Scrapy projects

Each of these is a standalone Scrapy project — `cd` into the folder and run `scrapy crawl <spider-name>`.

| Folder | Spider | Target | What it demonstrates |
| --- | --- | --- | --- |
| `amazon_data/` | `amazon_data_crawl` | amazon.in (Lenovo laptops) | Custom `User-Agent` headers, XPath on search-result cards, filtering by keyword |
| `computers/` | `scrap_computers` | webscraper.io test site | Static product + rating extraction, `response.follow` pagination |
| `web_scraper/` | `scraping` | webscraper.io (all-in-one) | Simple product/price/rating extraction |
| `products/` | `chocolatespider` | chocolate.co.uk | Extracting product cards from a real storefront |
| `api_project/` | `quotes`, `quote_login` | quotes.toscrape.com | Consuming a JSON API with pagination, and logging in with a CSRF-protected form (`FormRequest`) |
| `covidstats/` | `worldometers`, `audible`, `transcript` | worldometers.info, audible.com, subslikescript.com | Following links into detail pages, infinite/AJAX pagination, `CrawlSpider` + `LinkExtractor` rules |
| `flipkart/` | `flipkart_data` | flipkart.com (monitors) | Extracting titles, ratings, review counts from a JS-heavy listing |
| `apartment_data/` | `aramenia_datas` | list.am (Armenia rentals) | Rotating `User-Agent`s, Scrapy-Playwright rendering, `wait_for_selector` |
| `target/` | `target_data` | redsky.target.com API | Scraping a hidden JSON endpoint with query params, headers and cookies |
| `walmart_datas/` | `walmart_data` | walmart.com | Work-in-progress search scraper (bot protection encountered) |
| `laptops_data/` | `laptops` | webscraper.io (AJAX laptops) | Extracting product data from an embedded JSON payload (`data-items`) |

### Standalone scripts

| File | Description |
| --- | --- |
| `beautiful-soup/basics.py` | Beautiful Soup scraper that walks paginated movie listings on subslikescript.com and saves each transcript as a `.txt` file |
| `amazon/amazon_data.py` | `requests` + Beautiful Soup attempt at scraping Amazon search results (kept for comparison with the Scrapy version) |
| `playright_scraping/data_scrapjng.py` | Playwright script that searches arXiv and downloads result PDFs into `pdf/` |
| `scraping_hidden_api/target.py` | Hits Target's `plp_search_v2` API page-by-page and exports the results to Excel with pandas |

---

## Output data

Scraped results are checked into the repo alongside each project:

- `amazon_data/amazon_data.csv` — Lenovo laptop listings
- `computers/laptop_datas.csv` — laptop specs and reviews
- `products/*.csv`, `products/*.json` — chocolate product data
- `api_project/*.csv` — quotes (including paginated run)
- `covidstats/*.csv`, `covidstats/*.json` — country population, audible books, transcripts
- `flipkart/*.csv` — monitor listings and product details
- `apartment_data/armenia_apartment_datas.csv` — rental listings
- `scraping_hidden_api/target_multiple_pages.xlsx` — paginated Target results
- `playright_scraping/pdf/`, `playright_scraping/data/` — downloaded arXiv papers
- `beautiful-soup/*.txt` — movie transcripts

`states`, `states.csv` and `text.txt` are scratch files used for practising file I/O and not tied to a scraper.

---

## Setup

Requires **Python 3.10+**.

```bash
# from the repository root
python3 -m venv menv
source menv/bin/activate        # Windows: menv\Scripts\activate

pip install scrapy beautifulsoup4 requests lxml pandas openpyxl playwright
playwright install              # installs the Chromium browser used by Playwright spiders
```

## Running a scraper

**Scrapy project:**

```bash
cd amazon_data
scrapy crawl amazon_data_crawl -O output.csv
```

Replace `amazon_data` / `amazon_data_crawl` with any folder and spider from the table above.

**Standalone script:**

```bash
cd beautiful-soup
python basics.py

cd ../playright_scraping
python data_scrapjng.py
```

---

## Notes & caveats

- Selectors are site-specific and **will break** whenever a target site changes its markup.
- Several sites (Walmart, Flipkart, Amazon) employ bot detection; results may be empty or partial depending on rate and region.
- Cookies, tokens and `visitorId`s in `scraping_hidden_api/target.py` and `walmart_datas/walmart.py` are expired examples — supply your own if you re-run them, and keep them out of version control.
- `playright_scraping/geckodriver` is a bundled browser driver; the Playwright script itself only needs `playwright install`.
- Spiders that render JavaScript need Scrapy-Playwright enabled in the project's `settings.py` (`DOWNLOAD_HANDLERS` / `TWISTED_REACTOR`).
