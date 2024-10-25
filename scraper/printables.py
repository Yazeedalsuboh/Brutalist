from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import controller

models_objs = []

def scrape(prompt):
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get(f'https://www.printables.com/search/models?q={prompt}')

    html_content = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    models = soup.find_all('article', limit=10)
   
    if not models:
        print("No models found.")
    else:
        for models in models:
            image = models.find('picture', class_='svelte-11pdzs1 image-inside')
            image = image.find('img')['src']

            title = models.find('a', class_='h clamp-two-lines')

            model_obj = {
                "src": "printables",
                "title": title.text,
                "link": f'https://www.printables.com{title['href']}',
                "img": image
            }
            models_objs.append(model_obj)

        controller.add(models_objs)