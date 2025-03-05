import requests
from bs4 import BeautifulSoup

def scrape_recipe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scraping title
    title = soup.find("h1").text if soup.find("h1") else "No title found"
    
    # Scraping ingredients
    ingredients = []
    ingredients_section = soup.find('div', class_="ssrcss-1ynsflq-UnorderedList e1q8fsc70")
    if ingredients_section:
        ingredients_list = ingredients_section.find_all('li')
        for ingredient in ingredients_list:
            ingredients.append(ingredient.text.strip())
    # ingredients = [item.text for item in soup.find_all(class_="ssrcss-1ynsflq-UnorderedList e1q8fsc70")]
    # ingredients = [item.text for item in soup.find_all(class_="ingredient")]
    

    # Scraping steps
    steps = []
    steps_section = soup.find('div', class_='method')  # Adjust this based on your inspection
    if steps_section:
        steps_list = steps_section.find_all('li')
        for step in steps_list:
            steps.append(step.text.strip())  
    # steps = [step.text for step in soup.find_all(class_="step")]

    return {"title": title, "ingredients": ingredients, "steps": steps}
