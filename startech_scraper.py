from bs4 import BeautifulSoup
import requests
import csv

# Base URL of the webpage to scrape
base_url = 'https://www.startech.com.bd/laptop-notebook?filter_status=7&sort=p.price&order=ASC&limit=90&page='

# Open a CSV file to write the data
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['Product Name', 'Price'])

    # Iterate through pages 1 to 4
    for page in range(1, 5):
        # Construct the URL for the current page
        url = base_url + str(page)
        
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all product containers
        products = soup.find_all('div', class_='p-item')

        # Extract and write product data to the CSV file
        for product in products:
            product_name = product.find('h4', class_='p-item-name').text.strip()
            product_price = product.find('div', class_='p-item-price').text.strip().split()[0].replace('৳', '').replace(',', '')
            product_price = int(product_price)

            csvwriter.writerow([product_name, product_price])