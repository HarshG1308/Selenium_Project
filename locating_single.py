from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=122JQE8QWFE9P&sprefix=laptop%2Caps%2C220&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.text)
driver.close()
