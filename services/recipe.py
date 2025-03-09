import requests


class RecipeService:

    def __init__(self) -> None:
        self.__base_url = 'https://dummyjson.com'
        
    def get_recipes(self):
        response = requests.get(
            url=f'{self.__base_url}/recipes/',
        )
        return response.json()
    
    def get_recipe(self, recipe_id):
        response = requests.get(
            url=f'{self.__base_url}/recipes/{recipe_id}',
        )
        return response.json()
    
    def create_recipe(self, recipe):
        response = requests.post(
            url=f'{self.__base_url}/recipes/add',
            json=recipe
        )
        return response.json()
    
    def update_recipe(self, recipe_id, recipe):
        response = requests.put(
            url=f'{self.__base_url}/recipes/{recipe_id}',
            json=recipe
        )
        return response.json()
    
    def delete_recipe(self, recipe_id):
        response = requests.delete(
            url=f'{self.__base_url}/recipes/{recipe_id}',
        )
        return response.json()
    
    def search_recipes(self, search):
        response = requests.get(
            url=f'{self.__base_url}/recipes/search?q={search}',
        )
        return response.json()
    
    def sort_and_order_recipes(self, sort_by, order_by):
        response = requests.get(
            url=f'{self.__base_url}/recipes?sortBy={sort_by}&order={order_by}',
        )
        return response.json()
    
    def get_all_tags_recipes(self):
        response = requests.get(
            url=f'{self.__base_url}/recipes/tags',
        )
        return response.json()
    
    def get_recipes_by_tag(self, tag):
        response = requests.get(
            url=f'{self.__base_url}/recipes/tag/{tag}',
        )
        return response.json()
    
    def get_recipes_by_meal_type(self, meal_type):
        response = requests.get(
            url=f'{self.__base_url}/recipes/meal-type/{meal_type}',
        )
        return response.json()