from django.urls import path
from apps.recipes.views import recipes, recipe, sort_and_order_recipes, search_recipes, get_recipes_by_tag, get_recipes_by_meal_type


urlpatterns = [
    path('recipes/', recipes, name="recipes"),
    path('recipes/<int:recipe_id>', recipe, name="recipe"),
    path('recipes/sort/<str:tipo>', sort_and_order_recipes, name="sort_and_order_recipes"),
    path('recipes/search/', search_recipes, name="search_recipes"),
    path('recipes/tag/<str:tag>', get_recipes_by_tag, name="get_recipes_by_tag"),
    path('recipes/meal-type/<str:meal_type>', get_recipes_by_meal_type, name="get_recipes_by_meal_type"),
]