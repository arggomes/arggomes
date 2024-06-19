import requests
from bs4 import BeautifulSoup
import random
import time

# Function to fetch URLs from a file
def get_urls_from_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls if url.strip()]  # Remove empty lines and strip whitespace
    return urls

# Function to simulate clicking top 3 links on each URL
def simulate_web_traffic(urls):
    current_index = 0
    while True:
        url = urls[current_index]
        try:
            # Make a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links in the page
            links = soup.find_all('a')

            # Shuffle links to simulate random clicking
            random.shuffle(links)

            # Visit top 3 links
            for link in links[:3]:
                try:
                    # Visit the link (perform a GET request)
                    link_url = link.get('href')
                    if link_url and link_url.startswith('http'):
                        requests.get(link_url)
                        print(f"Visited link: {link_url}")
                        time.sleep(random.uniform(1, 5))  # Random sleep to simulate human behavior
                except Exception as e:
                    print(f"Error visiting link: {link.get('href')}, Error: {str(e)}")

        except Exception as e:
            print(f"Error fetching URL: {url}, Error: {str(e)}")

        # Move to the next URL in the list
        current_index = (current_index + 1) % len(urls)

if __name__ == "__main__":
    # Replace 'urls.txt' with the path to your file containing URLs
    urls = get_urls_from_file('urls.txt')

    # Simulate web traffic
    simulate_web_traffic(urls)
