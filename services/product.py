import requests


class ProductService:

    def __init__(self) -> None:
        self.__base_url = 'https://dummyjson.com'
        
    def get_products(self):
        response = requests.get(
            url=f'{self.__base_url}/products/',
        )
        return response.json()
    
    def get_product(self, product_id):
        response = requests.get(
            url=f'{self.__base_url}/products/{product_id}',
        )
        return response.json()
    
    def create_product(self, product):
        response = requests.post(
            url=f'{self.__base_url}/products/add',
            json=product
        )
        return response.json()
    
    def update_product(self, product_id, product):
        response = requests.put(
            url=f'{self.__base_url}/products/{product_id}',
            json=product
        )
        return response.json()
    
    def delete_product(self, product_id):
        response = requests.delete(
            url=f'{self.__base_url}/products/{product_id}',
        )
        return response.json()
    
    def search_products(self, search):
        response = requests.get(
            url=f'{self.__base_url}/products/search?q={search}',
        )
        return response.json()
    
    def sort_and_order_products(self, sort_by, order_by):
        response = requests.get(
            url=f'{self.__base_url}/products?sortBy={sort_by}&order={order_by}',
        )
        return response.json()
    
    def get_products_by_category(self, category):
        response = requests.get(
            url=f'{self.__base_url}/products/category/{category}',
        )
        return response.json()
    
    def get_category_list(self):
        response = requests.get(
            url=f'{self.__base_url}/products/category-list',
        )
        return response.json()