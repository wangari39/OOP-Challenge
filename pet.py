class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Yum!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Zzz...")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("-------------------------")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

my_pet = Pet("Buddy")

my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.show_tricks()

