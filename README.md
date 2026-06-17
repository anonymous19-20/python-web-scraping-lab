# Python Web Scraping Lab

A small Python practice repo for learning web scraping, HTML parsing, browser automation, and simple CSV export.

The examples here are intentionally simple. Some scripts read local HTML files with BeautifulSoup, some fetch live pages with Requests, and a couple use Selenium to drive Chrome and inspect pages after the browser has loaded them.

## What is inside

- `scripts/parse_local_example_link.py` reads a local Example Domain HTML file and prints its first link.
- `scripts/parse_apache_page_text.py` reads a saved Apache default page and prints the first paragraph.
- `scripts/fetch_example_links.py` fetches `example.com` and lists the links found on the page.
- `scripts/export_example_page_to_csv.py` saves the title, paragraph, and first link from `example.com` into a CSV file.
- `scripts/example_page_browser_check.py` compares a page heading from Requests with the title loaded by Selenium.
- `scripts/google_doodles_search.py` searches Google Doodles with Selenium and prints result links.
- `scripts/wikipedia_search_parser.py` searches Wikipedia with Selenium and prints paragraph text from the result page.
- `scripts/file_io_reference.py` is a small file-reading example.

## Project layout

```text
.
├── data/
│   ├── example_page_export.csv
│   └── sample_text.txt
├── samples/
│   ├── apache_default_page.html
│   ├── apache_default_page.css
│   ├── example_domain.html
│   └── example_domain.css
├── scripts/
│   └── Python examples
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

The Selenium examples also need Google Chrome and a compatible ChromeDriver available on your system.

## Running examples

```bash
cd scripts
python fetch_example_links.py
python export_example_page_to_csv.py
python parse_local_example_link.py
```

The CSV export script writes its output to `data/example_page_export.csv`.
