class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
specie = whiskers.species
hunger = whiskers.hunger
energy = whiskers.energy

print(f"Initial Attributes: Whiskers ({specie}) - Hunger: {hunger}, Energy: {energy}")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
new_hunger = whiskers.hunger = 3
#  - Increase energy by 2
new_energy = whiskers.energy = 10
# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: Whiskers ({specie}) - Hunger: {new_hunger}, Energy: {new_energy}")

