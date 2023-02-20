import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = 'https://www.wikipedia.org/'

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant data on the page
data = soup.find('div', {'class': 'content'}).text.strip()

# Write the data to a CSV file
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['data'])
    writer.writerow([data])
