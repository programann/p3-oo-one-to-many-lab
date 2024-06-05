class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        if pet.owner is not self:
            pet.owner = self  # This will handle adding the pet to the owner's list

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self._owner = None
        if owner:
            self.owner = owner  # use the owner setter to handle adding the pet to the owner's list
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if self._owner is not None:
            self._owner._pets.remove(self)
        self._owner = new_owner
        if new_owner is not None:
            new_owner._pets.append(self)

# Assuming you have the rest of your tests here, this should pass all of them.
