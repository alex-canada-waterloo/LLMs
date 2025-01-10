import requests
from bs4 import BeautifulSoup

# Specify the URL
url = 'https://python.langchain.com/docs/how_to/'

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all anchor tags
anchor_tags = soup.find_all('a')

# Extract the href attributes
links = [tag.get('href') for tag in anchor_tags if tag.get('href')]

# create output file
output_file = open("links.txt", "w")

# Print the list of links
for link in links:
    # if link starts with /docs/how_to then print it and append the base url
    if link.startswith('/docs/how_to'):
        # append the link into the file
        output_file.write(f"https://python.langchain.com{link}\n")
        print(f"https://python.langchain.com{link}")