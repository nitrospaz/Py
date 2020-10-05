# modified version of class activity

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self, song):
        for animal in self.animals:
            print(animal.sing(song))

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

    def sing(self, song):
        return f'{self.name} sings {song}'

cat1 = Cat('Simon', 4)

cat2 = Cat('Sally', 12)

#1 Add nother Cat
cat3 = Cat('Sam', 14)

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [cat1, cat2, cat3]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

#5 Make the cats sing Star Spangled Banner
my_pets.sing('Star Spangled Banner')

print(f'{cat1.sing("Voyager Theme Song")} and {cat2.name} hisses as Voyage jumps to warp')
