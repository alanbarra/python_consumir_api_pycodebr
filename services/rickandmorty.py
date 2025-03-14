import requests


class RickAndMortyService:

    def __init__(self) -> None:
        self.__base_url = 'https://rickandmortyapi.com/api'
        
    def get_all_characters(self, page=0):
        response = requests.get(
            url=f'{self.__base_url}/character/?page={page}',
        )
        return response.json()
    
    def get_character(self, character_id):
        response = requests.get(
            url=f'{self.__base_url}/character/{character_id}',
        )
        return response.json()
    
    def get_characters_by_status(self, status):
        response = requests.get(
            url=f'{self.__base_url}/character/?status={status}',
        )
        return response.json()
    
    def get_characters_by_species(self, species):
        response = requests.get(
            url=f'{self.__base_url}/character/?species={species}',
        )
        return response.json()
    
    def get_characters_by_gender(self, gender):
        response = requests.get(
            url=f'{self.__base_url}/character/?gender={gender}',
        )
        return response.json()
    
    def get_characters_by_name(self, search):
        response = requests.get(
            url=f'{self.__base_url}/character/?name={search}',
        )
        return response.json()