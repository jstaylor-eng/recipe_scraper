from django.http import JsonResponse
from scraper.scraper import scrape_recipe
from .models import Recipe, Ingredient

def fetch_recipe(request):
    url = request.GET.get("url")
    if not url:
        return JsonResponse({"error": "No URL provided"}, status=400)

    try:
        data = scrape_recipe(url)
    except Exception as e:
        return JsonResponse({"error": f"Failed to scrape recipe: {str(e)}"}, status=500)

    if not data.get("title") or not data.get("ingredients") or not data.get("steps"):
        return JsonResponse({"error": "Incomplete recipe data"}, status=400)


    recipe, created = Recipe.objects.get_or_create(title=data["title"], url=url)
    if created:
        for ingredient in data["ingredients"]:
            Ingredient.objects.create(name=ingredient, recipe=recipe)

    return JsonResponse({
        "title": recipe.title,
        "url": recipe.url,
        "ingredients": [ing.name for ing in recipe.ingredients.all()],
        "steps": data["steps"]
    })
