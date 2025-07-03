from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 20):  # Loop through the first 20 pages
    print(f"Fetching page {i}...")
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=122JQE8QWFE9P&sprefix=laptop%2Caps%2C220&ref=nb_sb_noss_2")

    elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    f = 1
    for item in elem:
        with open(f"data/item_{i}_{f}.html", "a") as file:
            file.write(item.get_attribute("outerHTML"))
        f += 1
    print(f"Total items found: {f}")

driver.close()
