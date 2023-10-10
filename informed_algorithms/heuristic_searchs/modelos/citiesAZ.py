from modelos.knowledgeRepresentation import City
from modelos.knowledgeRepresentation import Neighborhood


arad = City('Arad', 366)
bucharest = City('Bucharest', 0)
craiova = City('Craiova', 160)
dobreta = City('Dobreta', 242)
eforie = City('Eforie', 161)
fagaras = City('Fagaras', 178)
giurgiu = City('Giurgiu', 77)
hirsova = City('Hirsova', 151)
iasi = City('Iasi', 226)
lugoj = City('Lugoj', 244)
mehadia = City('Mehadia', 241)
neamt = City('Neamt', 234)
oradea = City('Oradea', 380)
pitesti = City('Pitesti', 98)
rimnicu_vilcea = City('Rimnicu Vilcea', 193)
sibiu = City('Sibiu', 253)
timisoara = City('Timisoara', 329)
urziceni = City('Urziceni', 80)
vaslui = City('Vaslui', 199)
zerind = City('Zerind', 374)

##Arad
arad.set_neig_citie(zerind, 75)
arad.set_neig_citie(sibiu, 140)
arad.set_neig_citie(timisoara, 118)
##Bucharest
bucharest.set_neig_citie(fagaras, 211)
bucharest.set_neig_citie(pitesti, 101)
bucharest.set_neig_citie(giurgiu, 90)
bucharest.set_neig_citie(urziceni, 85)
##Craiova
craiova.set_neig_citie(dobreta, 120)
craiova.set_neig_citie(rimnicu_vilcea, 146)
craiova.set_neig_citie(pitesti, 138)
##Dobreta
dobreta.set_neig_citie(mehadia, 75)
dobreta.set_neig_citie(craiova, 120)
##Eforie
eforie.set_neig_citie(hirsova, 86)
##Fagaras
fagaras.set_neig_citie(sibiu, 99)
fagaras.set_neig_citie(bucharest, 211)
##Giurgiu
giurgiu.set_neig_citie(bucharest, 90)
##Hirsova
hirsova.set_neig_citie(eforie, 86)
hirsova.set_neig_citie(urziceni, 98)
##Iasi
iasi.set_neig_citie(neamt, 87)
iasi.set_neig_citie(vaslui, 92)
##Lugoj
lugoj.set_neig_citie(timisoara, 111)
lugoj.set_neig_citie(mehadia, 70)
##Mehadia
mehadia.set_neig_citie(lugoj, 70)
mehadia.set_neig_citie(dobreta, 75)
##Neamt
neamt.set_neig_citie(iasi, 87)
##Oradea
oradea.set_neig_citie(zerind, 71)
oradea.set_neig_citie(sibiu, 151)
##Pitesti
pitesti.set_neig_citie(rimnicu_vilcea, 97)
pitesti.set_neig_citie(craiova, 138)
pitesti.set_neig_citie(bucharest, 101)
##Rimnicu Vilcea
rimnicu_vilcea.set_neig_citie(sibiu, 80)
rimnicu_vilcea.set_neig_citie(craiova, 146)
rimnicu_vilcea.set_neig_citie(pitesti, 97)
##Sibiu
sibiu.set_neig_citie(arad, 140)
sibiu.set_neig_citie(oradea, 151)
sibiu.set_neig_citie(rimnicu_vilcea, 80)
sibiu.set_neig_citie(fagaras, 99)
##Timisoara
timisoara.set_neig_citie(arad, 118)
timisoara.set_neig_citie(lugoj, 111)
##Urziceni
urziceni.set_neig_citie(bucharest, 85)
urziceni.set_neig_citie(hirsova, 98)
urziceni.set_neig_citie(vaslui, 142)
##Vaslui
vaslui.set_neig_citie(urziceni, 142)
vaslui.set_neig_citie(iasi, 92)
##Zerind
zerind.set_neig_citie(arad, 75)
zerind.set_neig_citie(oradea, 71)

neighborhood = Neighborhood()

neighborhood.set_city(arad)
neighborhood.set_city(bucharest)
neighborhood.set_city(craiova)
neighborhood.set_city(dobreta)
neighborhood.set_city(eforie)
neighborhood.set_city(fagaras)
neighborhood.set_city(giurgiu)
neighborhood.set_city(hirsova)
neighborhood.set_city(iasi)
neighborhood.set_city(lugoj)
neighborhood.set_city(mehadia)
neighborhood.set_city(neamt)
neighborhood.set_city(oradea)
neighborhood.set_city(pitesti)
neighborhood.set_city(rimnicu_vilcea)
neighborhood.set_city(sibiu)
neighborhood.set_city(timisoara)
neighborhood.set_city(urziceni)
neighborhood.set_city(vaslui)
neighborhood.set_city(zerind)

if __name__ == "__main__":
    print(arad.name)
    print(arad.neighbor_cities[0].name+' '+str(arad.path_cities[0]))
    print(arad.neighbor_cities[1].name + ' ' + str(arad.path_cities[1]))
    print(arad.neighbor_cities[2].name + ' ' + str(arad.path_cities[2]))

