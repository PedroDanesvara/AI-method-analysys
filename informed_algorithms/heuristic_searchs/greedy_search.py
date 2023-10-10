from modelos import citiesAZ

vicinity = citiesAZ.neighborhood


def greedySearch(start_city, final_city)->str:

    print("de: "+ start_city)
    indx_strt_city=0
    count=0
    present_city = start_city

    for city in vicinity.cities:
        if city.name == present_city:
            indx_strt_city=count
            break
        count+=1

    aux_charge=vicinity.cities[indx_strt_city].neighbor_cities[0].charge
    count=0
    less_expeinsive_city = 0

    for n_city in vicinity.cities[indx_strt_city].neighbor_cities:
        if n_city.name == final_city:
            print('Encontrou Destino: '+n_city.name)
            return n_city.name

        if n_city.charge < aux_charge:
            aux_charge=n_city.charge
            less_expeinsive_city = count

        count+=1
        present_city=vicinity.cities[indx_strt_city].neighbor_cities[less_expeinsive_city].name

    print('Cidades vizinhas:')
    for ct in vicinity.cities[indx_strt_city].neighbor_cities:
        print(ct.name +' '+ str(ct.charge))
    print('Vizinha mais barata = ' + present_city)
    print(' ')

    greedySearch(present_city, final_city)
