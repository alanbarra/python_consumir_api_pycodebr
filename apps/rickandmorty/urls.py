from django.urls import path
from apps.rickandmorty.views import characters, get_characters_by_status, get_characters_by_species, get_characters_by_gender, search_characters


urlpatterns = [
    path('characters/', characters, name="characters"),
    path('characters/status/<str:status>', get_characters_by_status, name="get_characters_by_status"),
    path('characters/species/<str:species>', get_characters_by_species, name="get_characters_by_species"),
    path('characters/gender/<str:gender>', get_characters_by_gender, name="get_characters_by_gender"),
    path('characters/search/', search_characters, name="search_characters"),
] 