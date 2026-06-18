# Python Web Scraping & Browser Automation Toolkit

A Python automation toolkit for web data extraction, dynamic page interaction,
and structured CSV export — built and tested on Kali Linux using Selenium,
BeautifulSoup4, and Requests inside an isolated virtual environment.

Covers static HTML parsing, live page fetching, JavaScript-rendered page
handling via ChromeDriver, and automated data pipeline output.

---

## Scripts

| Script | What it does |
|--------|-------------|
| `parse_local_example_link.py` | Parses a local HTML file with BeautifulSoup4 and extracts anchor tags |
| `parse_apache_page_text.py` | Parses a saved Apache2 default page and extracts paragraph content |
| `fetch_example_links.py` | Fetches a live page via Requests and enumerates all links |
| `export_example_page_to_csv.py` | Extracts title, paragraph, and link from a live page — exports structured CSV |
| `example_page_browser_check.py` | Cross-validates page heading between Requests response and Selenium-loaded DOM |
| `google_doodles_search.py` | Drives Chrome via Selenium to search Google Doodles and extract result URLs |
| `wikipedia_search_parser.py` | Automates Wikipedia search via Selenium and scrapes paragraph content from result page |
| `file_io_reference.py` | File I/O utility reference for pipeline integration |

---

## Project Layout

```text
.
├── data/
│   ├── example_page_export.csv     # Sample CSV output
│   └── sample_text.txt
├── samples/
│   ├── apache_default_page.html    # Saved Apache2 default page for offline parsing
│   ├── apache_default_page.css
│   ├── example_domain.html
│   └── example_domain.css
├── scripts/
│   └── *.py                        # All automation scripts
├── requirements.txt
└── README.md
```

---

## Setup

Tested on **Kali Linux** with Python 3.10+.

Create and activate an isolated virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Selenium scripts require **Google Chrome** and a matching **ChromeDriver** binary on your `$PATH`:

```bash
# Verify ChromeDriver is available
chromedriver --version
```

---

## Running

```bash
cd scripts

# Fetch live page and list links
python fetch_example_links.py

# Export structured data to CSV
python export_example_page_to_csv.py

# Parse local HTML file
python parse_local_example_link.py

# Browser automation — Google Doodles scraper
python google_doodles_search.py
```

CSV output is written to `data/example_page_export.csv`.

---

## Stack

| Tool | Role |
|------|------|
| `selenium` | Browser automation — dynamic/JS-rendered pages |
| `beautifulsoup4` | HTML parsing — static and saved pages |
| `requests` | HTTP fetching — live pages |
| `csv` (stdlib) | Structured data export |
| `venv` | Isolated dependency management |
| ChromeDriver | Headless/headed Chrome control via Selenium |

---

## Environment

Built and tested on **Kali Linux** · Python `venv` · VS Code with virtualenv-aware Code Runner
