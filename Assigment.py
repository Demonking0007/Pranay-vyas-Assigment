import openpyxl
from bs4 import BeautifulSoup

# Initialize lists to store the extracted data
product_data = []

# List of HTML files to process
html_files = ['Amazon.html', 'Amazon2.html', 'Amazon3.html']

for html_file in html_files:
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all div elements with the specified class
    product_divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section s-card-border')

    for div in product_divs:
        # Find the Product Name
        product_name_element = div.find('span', class_='a-size-medium a-color-base a-text-normal')
        product_name = product_name_element.get_text(strip=True) if product_name_element else " "

        # Find the Product Price
        product_price_element = div.find('span', class_='a-price-whole')
        product_price = product_price_element.get_text(strip=True) if product_price_element else " "

        # Find the Product Reviews
        product_reviews_element = div.find('span', class_='a-icon-alt')
        product_reviews = product_reviews_element.get_text(strip=True) if product_reviews_element else ""

        # Find the Product URL
        product_url_element = div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal', href=True)
        product_url = product_url_element['href'] if product_url_element else ""

        # Append the extracted data to the list
        product_data.append([product_name, product_price, product_reviews, product_url])

# Create a new Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Set headers for the Excel sheet
sheet['A1'] = 'Product Name'
sheet['B1'] = 'Product Price'
sheet['C1'] = 'Product Reviews'
sheet['D1'] = 'Product URL'

# Write the data to the Excel sheet
for row, product in enumerate(product_data, start=2):
    for col, value in enumerate(product, start=1):
        sheet.cell(row=row, column=col, value=value)

# Save the data to an Excel file
workbook.save('Amazon_Products.xlsx')

print("Data has been successfully written to Amazon_Products.xlsx.")
