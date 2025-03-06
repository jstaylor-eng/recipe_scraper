import requests
import json
from bs4 import BeautifulSoup

def scrape_recipe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    ldjson = json.loads("".join(soup.find("script", {"type": "application/ld+json"}).contents))

    # Find the recipe entry
    for item in ldjson.get('@graph', []):
        if item.get('@type') == 'Recipe':
            title = item.get('name', 'N/A')
            ingredients = item.get('recipeIngredient', [])
            steps = item.get('recipeInstructions', [])

    return {"title": title, "ingredients": ingredients, "steps": steps}
