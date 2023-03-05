# the codes.txt file is included, but here is the program to obtain it anyway

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the web page
driver.get('https://www.xe.com/currency/')

# Take all currencies and their codes
cur = driver.find_elements(By.TAG_NAME and By.CLASS_NAME, 'a' and 'currency__ListLink-sc-1xymln9-6')

# f string formatting does not support the use of \, hence why the separator need to be a variable
sep = '\n'

# Format the currencies
currencies = [f"{el.text.split(sep)[0]} {el.text.split(sep)[1]}" for el in cur]

for currency in currencies:
    with open('codes.txt', 'a', encoding="utf-8") as file:
        file.write(f"{currency}\n")