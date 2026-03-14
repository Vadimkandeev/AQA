class Animal:
    species = []

    def __init__(self, animal):
        self.add_species(animal)

        @classmethod
        def add_species(cls, animal):
            if animal not in cls.species:
                cls.species.append(animal)
        @classmethod
        def show_species(cls):
            return cls.species


