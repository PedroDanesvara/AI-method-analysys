from modelos import citiesAZ

vicinity = citiesAZ.neighborhood


def aStarSearch(start_city, final_city):

    print("de: " + start_city)
    indx_strt_city = 0
    count = 0
    present_city = start_city

    for neighbor in vicinity.cities:
        if neighbor.name == present_city:
            indx_strt_city = count
            break
        count += 1

    aux_f_x=vicinity.cities[indx_strt_city].neighbor_cities[0].charge + vicinity.cities[indx_strt_city].path_cities[0]
    count=0
    indx_less_expensive_neighbor = 0

    print('Vizinhas: ')
    for neighbor in vicinity.cities[indx_strt_city].neighbor_cities:

        if neighbor.name == final_city:
            print('Parou!')
            print('Encontrou Destino: '+neighbor.name)
            return neighbor.name

        f_x = neighbor.charge + vicinity.cities[indx_strt_city].path_cities[count]
        print(neighbor.name+'-> peso: '+ str(vicinity.cities[indx_strt_city].path_cities[count])
              +' + '+ str(neighbor.charge)+' = '+str(f_x))
        if f_x < aux_f_x:
            aux_f_x = f_x
            indx_less_expensive_neighbor =count
        count+=1

    present_city = vicinity.cities[indx_strt_city].neighbor_cities[indx_less_expensive_neighbor].name
    print('Mais barata: '+present_city)
    print(' ')

    aStarSearch(present_city,final_city)
