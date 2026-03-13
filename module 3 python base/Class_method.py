class Animal:
    species = []
    def add_species(self, animal):
        if animal not in self.species:
            self.species.append(animal)

    def show_species(self, species):
        return species
    def __init__(self):
        self.add_species()
        self.show_species()