import csv
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebScraper:
    """
    Scrape the mens clothings data from the daraz website
    """

    def __init__(self) -> None:
        self.link = "https://www.daraz.com.np/#"
        self.options = Options()
        # self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.data = {"item_name": [], "item_price": []}

    def convert_data_to_csv(self, file_name, pages):
        self.scrape_data(pages)
        df = pd.DataFrame(data=self.data)
        df.to_csv(f"{file_name}.csv")

    def scrape_data(self, pages):
        driver = self.driver
        driver.get(self.link)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#Level_1_Category_No9"))
        )
        driver.find_element(By.CSS_SELECTOR, "#Level_1_Category_No9").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#J_8018372580 > div > ul > ul.lzd-site-menu-sub.Level_1_Category_No9.lzd-site-menu-sub-active > li:nth-child(1)",
                )
            )
        )
        driver.find_element(
            By.CSS_SELECTOR,
            "#J_8018372580 > div > ul > ul.lzd-site-menu-sub.Level_1_Category_No9.lzd-site-menu-sub-active > li:nth-child(1)",
        ).click()
        i = 0
        while i < pages:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.gridItem--Yd0sa")
                )
            )
            items = driver.find_elements(By.CSS_SELECTOR, "div.gridItem--Yd0sa")
            for item in items:
                item_name = item.find_element(By.CSS_SELECTOR, "div.title--wFj93").text
                price = item.find_element(By.CSS_SELECTOR, "div.price--NVB62").text
                print(f"{item_name} -> {price}")
                self.data["item_name"].append(item_name)
                self.data["item_price"].append(price)

            driver.find_element(
                By.CSS_SELECTOR,
                "#root > div > div.ant-row.main--pIV2h > div:nth-child(1) > div > div.ant-col-20.ant-col-push-4.side-right--Tyehf > div.box--eTFFd > div > ul > li.ant-pagination-next > a",
            ).click()
            time.sleep(1)
            i += 1


if __name__ == "__main__":
    w = WebScraper()
    # w.scrape_data()
    w.convert_data_to_csv(file_name="mens_fashion", pages=20)
