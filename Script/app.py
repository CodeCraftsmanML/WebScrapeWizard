import os
import time
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging
from dotenv import load_dotenv

dotenv_path = r'S:\Data Analytics Interview\Web_Scrapping\Source\.env'
load_dotenv(dotenv_path=dotenv_path)

BASE_URL = os.getenv('BASE_URL')
CSV_FILE_LOCATION = os.getenv('CSV_FILE_LOCATION')
LOG_FILE_LOCATION = os.getenv('LOG_FILE_LOCATION')

# Debugging: Print loaded variables
print(f"BASE_URL: {BASE_URL}")
print(f"CSV_FILE_LOCATION: {CSV_FILE_LOCATION}")
print(f"LOG_FILE_LOCATION: {LOG_FILE_LOCATION}")

# Set up logging with custom format
logging.basicConfig(
    filename=LOG_FILE_LOCATION,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Custom format
    datefmt='%Y-%m-%d %H:%M:%S'  # Date format
)

def scrape_data():
    name = []
    return_1yr = []
    return_3yr = []
    return_5yr = []
    risk_type = []
    category = []

    for page_num in range(107):
        url = BASE_URL.format(page_num)
        logging.info(f"Scraping page {page_num + 1} / 107: {url}")

        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            fund = soup.find_all('tr', class_='f22Card')

            for i in fund:
                try:
                    name.append(i.find('div', class_='contentPrimary f22LH34 f22Mb4 truncate bodyBaseHeavy').text.strip())
                except AttributeError:
                    name.append(np.nan)

                try:
                    risk_type_text = i.find('div', class_='contentSecondary f22Ls2 bodySmallHeavy').text.strip()
                    risk_type.append(risk_type_text)
                except AttributeError:
                    risk_type.append(np.nan)

                try:
                    category_text = i.find_all('div', class_='contentSecondary f22Ls2 bodySmallHeavy')[1].text.strip()
                    category.append(category_text)
                except (IndexError, AttributeError):
                    category.append(np.nan)

                try:
                    returns = i.find_all('div', class_='contentPrimary center-align f22Mb4 bodyBaseHeavy')
                    return_1yr.append(returns[0].text.strip())
                    return_3yr.append(returns[1].text.strip())
                    return_5yr.append(returns[2].text.strip())
                except (IndexError, AttributeError):
                    return_1yr.append(np.nan)
                    return_3yr.append(np.nan)
                    return_5yr.append(np.nan)

            time.sleep(2)  # Delay between requests

        except Exception as e:
            logging.error(f"Error occurred: {e}")

    # Save data to CSV
    d = {
        'Mutual Fund Name': name,
        '1Y Return': return_1yr,
        '3Y Return': return_3yr,
        '5Y Return': return_5yr,
        'Risk Type': risk_type,
        'Category': category
    }
    df = pd.DataFrame(d)
    df.to_csv(CSV_FILE_LOCATION, index=False)
    logging.info(f"Data saved to {CSV_FILE_LOCATION}")

if __name__ == "__main__":
    scrape_data()
