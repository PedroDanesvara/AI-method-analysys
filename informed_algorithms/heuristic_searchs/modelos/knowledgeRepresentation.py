class City:

    def __init__(self, name, charge):
        self.name = name
        self.charge = charge
        self.neighbor_cities = []
        self.path_cities = []

    def get_name(self):
        return self.name

    def get_charge(self):
        return self.charge

    def set_neig_citie(self, city, distance):
        self.neighbor_cities.append(city)
        self.path_cities.append(distance)

    def get_num_neig_cities(self) -> int:
        return len(self.neighbor_cities)



class Neighborhood:

    cities = []

    def set_city(self, city):

        self.cities.append(city)

    def get_num_cities(self) -> int:
        return len(self.cities)


