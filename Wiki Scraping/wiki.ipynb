import requests
from bs4 import BeautifulSoup

def get_content(article_name):
    url = 'https://en.wikipedia.org/wiki/' + article_name
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find('div', {'id': 'mw-content-text', 'class': 'mw-body-content'})
    return content

def clean_content(content):
    # Initialize an empty list to store the cleaned content
    cleaned_content = []

    # Loop through the content and extract the text while excluding unwanted elements
    for element in content.find_all(['p', 'h2', 'h3']):
        # Remove any links and references from the text
        for link in element.find_all(['a', 'sup']):
            link.extract()
        # Append the remaining text to the cleaned_content list
        cleaned_content.append(element.get_text())

    return cleaned_content

data = get_content('Ozone_layer')
cleaned_data = clean_content(data)
for paragraph in cleaned_data:
    print(paragraph)
