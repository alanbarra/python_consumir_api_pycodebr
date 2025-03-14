from django.shortcuts import render, redirect
from services.rickandmorty import RickAndMortyService
import funcoes.sweetalert as sweetalert


def characters(request):
    try:
        service = RickAndMortyService()
        c = service.get_all_characters()
        characters = c['results']
        info = c['info']
        mensagem = 'Personagens Rick and Morty'
        sweetalert.mensagem(request, mensagem, 'success', 'toast')
        return render(request, 'characters/index.html', { "characters": characters, "info": info })
    except Exception as inst:
        mensagem = 'Erro ao buscar personagens. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    
def get_characters_by_status(request, status):
    try:
        service = RickAndMortyService()
        c = service.get_characters_by_status(status)
        characters = c['results']
        info = c['info']
        mensagem = 'Filtro efetuado, status: ', status
        sweetalert.mensagem(request, mensagem, 'success', 'toast')
        return render(request, 'characters/index.html', { "characters": characters, "info": info })
    except Exception as inst:
        mensagem = 'Erro ao buscar personagens. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    
def get_characters_by_species(request, species):
    try:
        service = RickAndMortyService()
        c = service.get_characters_by_species(species)
        characters = c['results']
        info = c['info']
        mensagem = 'Filtro efetuado, espécie: ', species
        sweetalert.mensagem(request, mensagem, 'success', 'toast')
        return render(request, 'characters/index.html', { "characters": characters, "info": info })
    except Exception as inst:
        mensagem = 'Erro ao buscar personagens. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    

def get_characters_by_gender(request, gender):
    try:
        service = RickAndMortyService()
        c = service.get_characters_by_gender(gender)
        characters = c['results']
        info = c['info']
        mensagem = 'Filtro efetuado, gênero: ', gender
        sweetalert.mensagem(request, mensagem, 'success', 'toast')
        return render(request, 'characters/index.html', { "characters": characters, "info": info })
    except Exception as inst:
        mensagem = 'Erro ao buscar personagens. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
    
def search_characters(request): 
    try:
        pesquisa = request.GET['search']
        if "search" in request.GET:
            service = RickAndMortyService()
            c = service.get_characters_by_name(pesquisa)
            characters = c['results']
            info = c['info']
            mensagem = 'Pesquisa efetuada: ', pesquisa
            sweetalert.mensagem(request, mensagem, 'success', 'toast')
            return render(request, 'characters/index.html', { "characters": characters, "info": info })
    except Exception as inst:
        mensagem = 'Erro ao pesquisar personagens. Erro: ', inst
        sweetalert.mensagem(request, mensagem, 'error', 'toast')
        return redirect('')
