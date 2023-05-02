from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

print("""Welcome to this currency converter.
Please always enter the currency by its code (e.g. USD or EUR).\n""")

print("Here is a list of all currencies and their codes.")
with open('D:\codene\Python\currency_converter\Currency-Converter\codes.txt', 'r') as file:
    for line in file.readlines():
        print(line)


# Take user input
from_currency = input('Enter the currency you want to convert from: ')
to_currency = input('Enter the currency you want to convert to: ')
amount = input('Enter the amount: ')

# Access the page using the user input
url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"

# Navigate to the page
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(5)

# Print the result
try:
    result_from = driver.find_element(By.TAG_NAME and By.CLASS_NAME, 'p' and 'result__ConvertedText-sc-1bsijpp-0').text
    result_to = driver.find_element(By.TAG_NAME and By.CLASS_NAME, 'p' and 'result__BigRate-sc-1bsijpp-1').text

    print(f"\n{result_from} {result_to}")
except NoSuchElementException:
    print("Invalid input!")
