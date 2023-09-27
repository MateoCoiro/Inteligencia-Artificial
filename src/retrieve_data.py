import re
from time import sleep

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_numeric_values(url, driver, class_name):
    driver.get(url)
    modelo_class_elements = driver.find_elements(By.CSS_SELECTOR, class_name)
    for element in modelo_class_elements:
        # Para datos
        href_attribute = element.get_attribute('href')
        driver.get(href_attribute)
        div_element = driver.find_element(By.CSS_SELECTOR, "col-12")
        print(div_element.text)

        # Para imagenes
        # img_element = element.find_element(By.TAG_NAME, 'img')
        # src_attribute = img_element.get_attribute('src')
        # get_image(src_attribute)


def get_image(link):
    return


def run(class_name):
    url_marca = 'https://www.ultimatespecs.com/es/car-specs/Ford-models'
    # Create a WebDriver instance (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Load the page
    driver.get(url_marca)
    modelo_class_elements = driver.find_elements(By.CSS_SELECTOR, class_name)

    # Create a list to store href attributes
    modelos_href_attributes = []

    for element in modelo_class_elements:
        href_attribute = element.get_attribute('href')
        modelos_href_attributes.append(href_attribute)

    # Iterate through the href attributes and visit each page
    for modelo_href_attribute in modelos_href_attributes:
        driver.get(modelo_href_attribute)
        print("Esperando")
        variantes_href_attributes  = []
        # Now you can extract data from the current page
        variantes_class_elements = driver.find_elements(By.CSS_SELECTOR, class_name)

        for element in modelo_class_elements:
            href_attribute = element.get_attribute('href')
            variantes_href_attributes.append(href_attribute)

        for variante_href_attribute in variantes_href_attributes:
            driver.get(variante_href_attribute)

            # Extract data from the current page as needed
            div_element = driver.find_element(By.CLASS_NAME, "col-12")
            print(div_element.text)

    # Close the browser when done
    driver.quit()

modelo_class_name = ".col-md-3.col-sm-4.col-xs-4.col-4"

run(modelo_class_name)