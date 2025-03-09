from django.shortcuts import render, redirect
from services.recipe import RecipeService
import funcoes.sweetalert as sweetalert


def recipes(request):
    try:
        service = RecipeService()
        r = service.get_recipes()
        recipes = r['recipes']
        tags = service.get_all_tags_recipes()
        return render(request, 'recipes/index.html', { "recipes": recipes, "tags": tags })
    except Exception as inst:
        mensagem = 'Erro ao buscar receitas. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    
    
def sort_and_order_recipes(request, tipo):
    try:
        service = RecipeService()
        tags = service.get_all_tags_recipes()
        sort_by = tipo
        if tipo == 'rating':
            order_by = 'desc'
        else:
            order_by = 'asc'
        r = service.sort_and_order_recipes(sort_by, order_by)
        recipes = r['recipes']
        return render(request, 'recipes/index.html', { "recipes": recipes, "tags": tags })
    except Exception as inst:
        mensagem = 'Erro ao ordenar receitas. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')


def search_recipes(request): 
    try:
        if "search" in request.GET:
            pesquisa = request.GET['search']
            service = RecipeService()
            tags = service.get_all_tags_recipes()
            r = service.search_recipes(pesquisa)
            recipes = r['recipes']
            return render(request, 'recipes/index.html', { "recipes": recipes, "tags": tags })
    except Exception as inst:
        mensagem = 'Erro ao pesquisar receitas. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    
    
def recipe(request, recipe_id):
    try:
        service = RecipeService()
        tags = service.get_all_tags_recipes()
        recipe = service.get_recipe(recipe_id)
        return render(request, 'recipes/show.html', { "recipe": recipe, "tags": tags })
    except Exception as inst:
        mensagem = 'Erro ao buscar receita. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
        
        
def get_recipes_by_tag(request,tag):
    try:
        service = RecipeService()
        tags = service.get_all_tags_recipes()
        r = service.get_recipes_by_tag(tag)
        recipes = r['recipes']
        return render(request, 'recipes/index.html', { "recipes": recipes, "tags": tags })
    except Exception as inst:
        mensagem = 'Erro ao buscar receita. por tag. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')


def get_recipes_by_meal_type(request, meal_type):
    try:
        service = RecipeService()
        tags = service.get_all_tags_recipes()
        r = service.get_recipes_by_meal_type(meal_type)
        recipes = r['recipes']
        return render(request, 'recipes/index.html', { "recipes": recipes, "tags": tags })
    except Exception as inst:
        mensagem = 'Erro ao buscar receitas por tipo de refeição. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    