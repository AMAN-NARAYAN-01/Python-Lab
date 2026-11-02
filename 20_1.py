import requests
from bs4 import BeautifulSoup

# Target URL (using Hacker News as a clean example)
url = "https://news.ycombinator.com/"

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find elements containing the headlines and links
    headlines = soup.find_all('span', class_='titleline')

    # Extract and print each headline and its corresponding URL
    for item in headlines:
        link_tag = item.find('a')
        if link_tag:
            headline = link_tag.get_text()
            hyperlink = link_tag.get('href')
            print(f"Headline: {headline}")
            print(f"Link: {hyperlink}\n")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")