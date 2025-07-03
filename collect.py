import os
import pandas as pd
from bs4 import BeautifulSoup

# Path to the data folder
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# List to store product details
data = []

# Loop through all HTML files in the data directory
for filename in os.listdir(DATA_DIR):
    try:
        if filename.endswith('.html'):
            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                title = soup.find('h2')
                data.append({
                    'title': title.get_text(),
                    'link': "https://www.amazon.in/" + soup.find("a")['href'],
                    'price': soup.find("span", class_="a-price-whole").getText()
                })
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

# Create DataFrame
products_df = pd.DataFrame(data)

# Save to CSV (optional)
products_df.to_csv('products.csv', index=False)

# Print the DataFrame
print(products_df)

