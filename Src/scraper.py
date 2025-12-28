import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_valmont(urls, driver_options):
    # Initialize driver inside the function
    driver = webdriver.Chrome(options=driver_options)
    all_products = []

    try:
        for url in urls:
            print(f"Scraping Listing Page: {url}")
            driver.get(url)
            # Wait specifically for the product container to load
            wait = WebDriverWait(driver, 15)
            try:
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "js-product-miniature-wrapper")))
            except:
                print(f"Timeout or no products found on {url}")
                continue

            product_elements = driver.find_elements(By.CLASS_NAME, "js-product-miniature-wrapper")
            product_links = []
            for p in product_elements:
                try:
                    link = p.find_element(By.CSS_SELECTOR, "h2.product-title a").get_attribute("href")
                    product_links.append(link)
                except:
                    continue

            for link in product_links:
                try:
                    driver.get(link)
                    name = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text.strip()
                    
                    try:
                        price = driver.find_element(By.CSS_SELECTOR, "span.product-price").get_attribute("content")
                    except:
                        price = "N/A"

                    capacity_pattern = r"(\d+\s*(?:ml|m|pezzo|pezzi|duo))"
                    match = re.search(capacity_pattern, name, re.IGNORECASE)
                    capacity = match.group(1) if match else None

                    if not capacity:
                        try:
                            # Use JS to click the description to ensure it works even if overlapped
                            desc_trigger = driver.find_element(By.CSS_SELECTOR, "a[href='#productdaas-accordion-description']")
                            driver.execute_script("arguments[0].click();", desc_trigger)
                            time.sleep(1)
                            desc_content = driver.find_element(By.CSS_SELECTOR, "#productdaas-accordion-description .rte-content")
                            desc_text = desc_content.get_attribute("textContent").strip()
                            desc_match = re.search(capacity_pattern, desc_text, re.IGNORECASE)
                            if desc_match:
                                capacity = desc_match.group(1)
                        except:
                            pass

                    all_products.append({
                        "product_name": name,
                        "price": price,
                        "capacity": capacity if capacity else "N/A",
                        "product_url": link
                    })
                except Exception as e:
                    print(f"Error on product {link}: {e}")
    finally:
        driver.quit()

    return all_products