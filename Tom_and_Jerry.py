import random

class TomandJerry:
    def __init__(self):
        self.num_doors = 50
        self.house_map = self.generate_house_map()
        self.Jerry = random.randint(1, self.num_doors)
        self.Tom = random.choice([door for door in range(1, self.num_doors +1) if door != self.Jerry])
        self.Trap = random.sample([door for door in range(1, self.num_doors +1) if door != self.Jerry and door != self.Tom], 5)
        self.Dog = random.sample([door for door in range(1, self.num_doors +1) if door not in self.Trap and door != self.Jerry and door != self.Tom], 5)
        self.Fridge = random.choice([door for door in range(1, self.num_doors + 1) if door not in [self.Jerry, self.Tom] + self.Trap + self.Dog])

    def generate_house_map(self):
        house_map = {door: [] for door in range(1, self.num_doors + 1)}
        for door in range(1, self.num_doors + 1):
            while len(house_map[door]) < 3:
                neighbor = random.randint(1, self.num_doors)
                if neighbor != door and neighbor not in house_map[door]:
                    house_map[door].append(neighbor)
                    house_map[neighbor].append(door)
        return house_map
    
    def display_info(self):
        print(f"Jerry choose a door {self.Jerry}")
        print(f"The corridor leads to{self.house_map[self.Jerry]}.")

    def move_Jerry(self, door):
        if door in self.house_map[self.Jerry]:
            self.Jerry = door
        else:
            print("Invalid move! Try again.")

    

    def check_door(self):
        if self.Jerry == self.Tom:
            print("Tom is behind the door! Jerry gets caught.")
            return True
        elif self.Jerry in self.Trap:
            print("It's a mouse trap! Jerry gets caught.")
            return True
        elif self.Jerry in self.Dog:
            print("It the dog! Jerry get a shortcut to the fridge.")
            self.Jerry = random.randint(1, self.num_doors)
        elif self.Jerry == self.Fridge:
            print("Jerry finds the cheese and wins!")
            return True
        else:
            print(f"The room is safe.Jerry continues {self.Jerry}.")
        return False
    
    def sense_danger(self):
        for neighbor in self.house_map[self.Jerry]:
            if neighbor == self.Tom:
                print("You can hear Tom purring.")
            if neighbor in self.Trap:
                print("You hear snapping")
            if neighbor in self.Dog:
                print("You hear barking")
    
    def play(self):
        print("Start Game: Jerry's Quest for the Cheese")
        print("Navigate the house to get to the Fridge and get cheese. Beware of Tom and mouse traps but the Dog will help you.")
        while True:
            self.display_info()
            self.sense_danger()
            move = input("Where to? (Open door number): ")
            try:
                move = int(move)
                if move < 1 or move > self.num_doors:
                    print(f"Invalid door! Enter a number between 1 and {self.num_doors}.")
                    continue
                self.move_Jerry(move)
                if self.check_door():
                    print("Game Over!")
                    break
            except ValueError:
                print("Please enter a valid door number.")

game = TomandJerry()
game.play()

        
