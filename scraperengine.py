import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class StartupScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_site(self, soup, container_tag, container_class, title_tag, title_class):
        results = []
        items = soup.find_all(container_tag, class_=container_class)
        for item in items:
            title_element = item.find(title_tag, class_=title_class)
            if title_element:
                results.append({'Title': title_element.text.strip()})
        return results

    def get_next_page(self, soup, current_url):
        next_button = soup.find('li', class_='next')
        if next_button and next_button.find('a'):
            next_link = next_button.find('a')['href']
            return urljoin(current_url, next_link)
        return None