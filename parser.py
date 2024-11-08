import requests
from bs4 import BeautifulSoup
import json
import logging
from time import sleep

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_quotes():
    base_url = "https://quotes.toscrape.com"
    quotes_data = []
    page = 1
    
    try:
        while True:
            url = f"{base_url}/page/{page}/"
            logger.info(f"Обработка страницы {page}")
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                quotes = soup.find_all('div', class_='quote')
                
                if not quotes:
                    break
                    
                for quote in quotes:
                    quote_data = {
                        'text': quote.find('span', class_='text').text.strip('""'),
                        'author': quote.find('small', class_='author').text,
                        'tags': [tag.text for tag in quote.find_all('a', class_='tag')]
                    }
                    quotes_data.append(quote_data)
                
                page += 1
                sleep(1)  # Добавляем задержку между запросами
                
            except requests.RequestException as e:
                logger.error(f"Ошибка при запросе страницы {page}: {e}")
                break
                
    except Exception as e:
        logger.error(f"Произошла непредвиденная ошибка: {e}")
    
    logger.info(f"Всего собрано цитат: {len(quotes_data)}")
    return quotes_data

def save_to_json(data, filename='quotes.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.info(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        logger.error(f"Ошибка при сохранении данных: {e}")

if __name__ == "__main__":
    quotes = get_quotes()
    save_to_json(quotes)
