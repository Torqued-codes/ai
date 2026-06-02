import pandas as pd
import os
from scraperengine import StartupScraper
from analyzer import SentimentAnalyzer

def main():
    base_url = "http://books.toscrape.com/"
    current_url = base_url
    
    CONFIG = {
        'container_tag': 'article',
        'container_class': 'product_pod',
        'title_tag': 'h3',
        'title_class': None 
    }
    
    
    all_data = []
    scraper = StartupScraper(base_url)
    analyzer = SentimentAnalyzer()

    while current_url:
        print(f"Scraping: {current_url}")
        soup = scraper.fetch_page(current_url)
        
        if not soup: 
            break
            
        page_data = scraper.parse_site(soup, **CONFIG)
    
        for item in page_data:
            item['Sentiment'] = analyzer.get_sentiment(item['Title'])
            all_data.append(item)
            
        current_url = scraper.get_next_page(soup, current_url)
    

    df = pd.DataFrame(all_data)
    os.makedirs('data', exist_ok=True)
    output_path = os.path.join('data', 'sentiment_results.csv')
    df.to_csv(output_path, index=False)
    print(f"Success! Collected and analyzed {len(df)} items. Data saved to {output_path}")

if __name__ == "__main__":
    main()




