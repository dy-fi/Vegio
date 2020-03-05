import requests
import json



# recipe search URL
recipe_search = "https://api.spoonacular.com/recipes/search"
recipe_info_base = "https://api.spoonacular.com/recipes/"

apiKey = '5be98f9487da4053964aa2e66b5bb3d1'


def get_food_recipe(food, exclude=None, intolerances=None):
    """
    Query based on user input, request relevant data
    """

    # initial query
    params = {
        "apiKey": apiKey,
        "query": food,
        "diet": "Vegetarian"
    }
    # optionals
    # if exclude: params["excludeIngredients"] = exclude
    # if intolerances: params["intolerances"] = intolerances
    
    # make request and load JSON into python object
    resp = requests.get(recipe_search, params=params)
    recipes = resp.json()

    result = []
    # find info for each recipe, and append to result
    try:
        if recipes["code"] == 402:
            print(recipes)
            return
    except:
        pass

    for recipe in recipes["results"]:
        params = {
            "apiKey": apiKey
        }
        # recipe request
        resp = requests.get(recipe_info_base + str(recipe["id"]) + "/information", params=params).json()
        # data formatting
        data = {
            "title": resp["title"],
            "summary": resp["summary"],
            "image_url": resp["image"],
            "source_url": resp["sourceUrl"],
            "spoon_id": recipe["id"]
        }

        result.append(data)

    print(result)
    return result

if __name__ == '__main__':
    print(get_food_recipe("burger"))
