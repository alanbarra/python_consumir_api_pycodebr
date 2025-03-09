import requests


class FeriadoService:
    
    def __init__(self) -> None:
        self.__base_url = 'https://holidays.abstractapi.com/v1/'
        
    def get_feriado(self, dados):
        response = requests.request(
            "GET",
            url=f'{self.__base_url}',
            params=dados
        )
        return response.json()