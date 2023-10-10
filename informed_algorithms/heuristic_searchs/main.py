import greedy_search
import a_star_search


if __name__ == "__main__":

    cidade_inicial = 'Arad'
    #cidades_destino = 'Neamt'
    cidades_destino = 'Bucharest'

    print('Inicio:'+cidade_inicial)
    print('Destino: ' + cidades_destino)
    print('----------------------')
    greedy_search.greedySearch(cidade_inicial, cidades_destino)
    a_star_search.aStarSearch(cidade_inicial, cidades_destino)

