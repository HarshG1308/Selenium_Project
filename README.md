# Selenium Product Scraper

This project scrapes product listings from Amazon India using Selenium, saves each product's HTML to a local `data/` folder, and then parses these files to create a structured dataset (CSV) with product details using pandas and BeautifulSoup.

## Features
- Scrapes multiple pages of Amazon search results for a given query (default: `laptop`).
- Saves each product's HTML snippet as a separate file in the `data/` directory.
- Parses all saved HTML files to extract product title, price, and other details.
- Aggregates the data into a pandas DataFrame and exports it as `products.csv`.

## Requirements
- Python 3.7+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Python packages:
  - selenium
  - pandas
  - beautifulsoup4

## Setup
1. **Clone the repository** (if using git):
   ```bash
   git clone <your-repo-url>
   cd Selenium_Project
   ```
2. **Install dependencies:**
   ```bash
   pip install selenium pandas beautifulsoup4
   ```
3. **Download ChromeDriver:**
   - Download from: https://sites.google.com/a/chromium.org/chromedriver/downloads
   - Place the `chromedriver` executable in your PATH or in the project directory.

## Usage

### 1. Scrape Product HTML
Run the following script to scrape product listings from Amazon and save them as HTML files:

```bash
python locating_multiple.py
```

- This will create files like `data/item_1_1.html`, `data/item_1_2.html`, ... for each product on each page.

### 2. Parse and Collect Data
Run the following script to parse all HTML files and create a CSV of product details:

```bash
python collect.py
```

- This will generate `products.csv` with columns like `title`, `price`, and other extracted details.

## File Overview
- `locating_multiple.py`: Scrapes Amazon and saves product HTML files.
- `collect.py`: Parses saved HTML files and creates a CSV dataset.
- `data/`: Directory containing all scraped product HTML files.

## Notes
- The HTML structure of Amazon may change over time. You may need to update the selectors in `collect.py` to match the current structure.
- Use responsibly and respect Amazon's terms of service.

## License
This project is for educational purposes only.
