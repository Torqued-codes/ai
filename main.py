import pandas as pd
import os
from scraperengine import StartupScraper
from analyzer import SentimentAnalyzer

def main():
    URL = "http://books.toscrape.com/"
    CONFIG = {
        'container_tag': 'article',
        'container_class': 'product_pod',
        'title_tag': 'h3',
        'title_class': None 
    }
    
    scraper = StartupScraper(URL)
    soup = scraper.fetch_page(URL)
    raw_data = scraper.parse_site(soup, **CONFIG)
    
    analyzer = SentimentAnalyzer()
    for item in raw_data:
        item['Sentiment'] = analyzer.get_sentiment(item['Title'])
    
    df = pd.DataFrame(raw_data)
    os.makedirs('data', exist_ok=True)
    output_path = os.path.join('data', 'sentiment_results.csv')
    df.to_csv(output_path, index=False)
    print(f"Success! Analyzed data saved to {output_path}")

if __name__ == "__main__":
    main()