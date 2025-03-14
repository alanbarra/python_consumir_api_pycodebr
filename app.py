from services.feriado import FeriadoService
from services.cep import CepService
from services.product import ProductService
from services.recipe import RecipeService
from services.rickandmorty import RickAndMortyService

#------------------------------ Consulta Feriados --------
#dados = {
#    "country":"br",
#    "api_key":"xxxxx",
#    "year":2025,
#    "month":3,
#    "day":3
#}

#service = FeriadoService()
#feriado = service.get_feriado(dados)
#print(feriado)


#----------------------------- Consulta CEP --------------
#cep = 11050200
#service = CepService(cep)
#endereco = service.busca_cep()
#print(endereco['logradouro'])
#print(endereco['bairro'])
#print(endereco['localidade'])
#print(endereco['estado'])

#--------------------------- Products--------------------
#service = ProductService()
#p = service.get_products()
#print(p)

#service = ProductService()
#p = service.get_product(1)
#print(p['title'])
#print(p['description'])
#print(p['category'])
#print(p['price'])
#print(p['discountPercentage'])
#print(p['rating'])
#print(p['stock'])
#print(p['tags'])
#print(p['brand'])
#print(p['sku'])
#print(p["images"][0])

#product = {
#    'title': 'teste 2',
#    'description': 'teste de inclusao 2',
#    'category': 'outra'
#}
#service = ProductService()
#create_product = service.create_product(product=product)
#print(create_product)

#product = {
#    'title': 'teste 2',
#    'description': 'teste de inclusao 2',
#    'category': 'outra'
#}
#product_id = 19
#service = ProductService()
#update_product = service.update_product(product_id, product=product)
#print(update_product)

#product_id = 1
#service = ProductService()
#delete_product = service.delete_product(product_id)
#print(delete_product)

#search = 'PHONE'
#service = ProductService()
#search_products = service.search_products(search)
#print(search_products)

#sort_by = 'price'
#order_by = 'asc'   # desc or asc
#service = ProductService()
#sort_and_order_products = service.sort_and_order_products(sort_by, order_by)
#print(sort_and_order_products)

#category = "vehicle"
#service = ProductService()
#get_products_by_category = service.get_products_by_category(category)
#print(get_products_by_category)

#service = ProductService()
#get_category_list = service.get_category_list()
#for category in get_category_list:
#    print(category)

#--------------------------- Recipes --------------------
#service = RecipeService()
#recipes = service.get_recipes()
#print(recipes)

#service = RecipeService()
#recipe = service.get_recipe(50)
#print(recipe)

#recipe = {
#    'name': 'teste 2',
#    'ingredients': 'teste de inclusao 2',
#}
#service = RecipeService()
#create_recipe = service.create_recipe(recipe=recipe)
#print(create_recipe)

#recipe = {
#    'name': 'teste 2',
#    'ingredients': 'teste de inclusao 2',
#}
#recipe_id = 19
#service = RecipeService()
#update_recipe = service.update_recipe(recipe_id, recipe=recipe)
#print(update_recipe)

#recipe_id = 1
#service = RecipeService()
#delete_recipe = service.delete_recipe(recipe_id)
#print(delete_recipe)

#search = 'pasta'
#service = RecipeService()
#search_recipes = service.search_recipes(search)
#print(search_recipes)

#sort_by = 'name'
#order_by = 'asc'   # desc or asc
#service = RecipeService()
#sort_and_order_recipes = service.sort_and_order_recipes(sort_by, order_by)
#print(sort_and_order_recipes)

#service = RecipeService()
#all_tags_recipes = service.get_all_tags_recipes()
#for tag in all_tags_recipes:
#    print(tag)
    
#tag = "japanese"
#service = RecipeService()
#get_recipes_by_tag = service.get_recipes_by_tag(tag)
#print(get_recipes_by_tag)

#meal_type = "dinner"
#service = RecipeService()
#get_recipes_by_meal_type = service.get_recipes_by_meal_type(meal_type)
#print(get_recipes_by_meal_type)

#service = RickAndMortyService()
#get_all_characters = service.get_all_characters()
#print(get_all_characters)

character_id = 50
service = RickAndMortyService()
get_character = service.get_character(character_id)
print(get_character)