# Currency-Converter
 This is a Python script that allows you to convert between currencies using the [XE currency converter website](https://www.xe.com/currencyconverter/). The script uses the Selenium package to navigate to the website, input the currencies and amount, and retrieve the conversion result.

## Getting started

Before running the script, make sure you have the following installed:

- Python 3.x
- Selenium package for Python
- Chrome driver

You can download Chrome driver from the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads). Once downloaded, add the location of the driver to your system PATH.

To install Selenium, run the following command in your terminal: pip install selenium

## Usage

1. Run the `currency_codes.py` file first to get a list of all the currency codes. This will create a `codes.txt` file with a list of all the available currencies and their codes.

2. Run the `currency_converter.py` file and follow the prompts. Enter the currency you want to convert from, the currency you want to convert to, and the amount.

3. The script will then navigate to the XE currency converter website, input the currencies and amount, and retrieve the conversion result.

## Notes

- The script uses `input()` function to take user input, so make sure to enter the currencies and amount when prompted.

- The script only works with currency codes, not currency names.

- The script may not work if the XE currency converter website layout changes.

- The script saves the currency codes to a file called `codes.txt`. This file is created in the same directory as the script. If you run the `currency_codes.py` file multiple times, the codes will be appended to the end of the file. 

- The script uses `implicitly_wait()` function to wait for the page to load. This function will wait for up to 5 seconds for the page to load before raising an exception. If the page takes longer to load, you may need to increase the wait time.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
