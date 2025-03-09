import requests


class CepService:
    
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP é inválido !!")
        
    def __str__(self):
        return self.format_cep()
        
    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def busca_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        response = requests.get(url)
        return response.json()