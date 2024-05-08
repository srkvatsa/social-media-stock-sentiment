"""
@author: Srivatsa Kundurthy

This program scrapes Gab posts mentioning the keyword "Nvidia". 
It uses a custom reverse engineered API endpoint. 
"""

import requests
from bs4 import BeautifulSoup

def scrape_website(url, output_file):
    # Set the user agent to Mozilla
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        

        text_content = soup.get_text()
        

        with open(output_file, 'w') as file:
            file.write(text_content)
            
        print(f"Scraping successful! Content written to {output_file}")
    else:
        print("Failed to scrape the website.")



query = "nvidia"

for i in range(1,21):
    url = f"https://gab.com/api/v3/search?type=status&onlyVerified=false&q={query}&resolve=true&page={i}"
    output_file = f"demo_gen/output{i}.txt"
    scrape_website(url, output_file)
output_file = "output.txt"
scrape_website(url, output_file)