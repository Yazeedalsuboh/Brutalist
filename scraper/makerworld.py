from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import controller

models_objs = []


def scrape(prompt):
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(f'https://makerworld.com/en/search/models?keyword={prompt}')

    html_content = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    models_grid = soup.find('div', class_= 'portal-css-ufcztx')
    models = models_grid.find_all('div', class_='portal-css-0', limit=10)
    
    if not models:
        print("No models found.")
    else:
        for model in models:
            image_grid = model.find('div', class_='design-cover-wrap portal-css-16eo00i')
            image = image_grid.find('img')['src']

            title_grid = model.find('div', class_='MuiStack-root portal-css-t4waze')
            title = title_grid.find('a')

            model_obj = {
                "src": "makerworld",
                "title": title.text,
                "link": f'https://makerworld.com{title['href']}',
                "img": image
            }
            models_objs.append(model_obj)
        
        controller.add(models_objs)