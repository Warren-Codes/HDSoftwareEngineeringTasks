class Wolf:
    # Class variables
    classification = "canine"
    habitat = "forest"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    # First object, set up instance variables of constructor method
    silver_tooth = Wolf("Silvertooth", 5)
    # Print out instance variable name
    print(silver_tooth.name)
    # Print out class variable habitat
    print(silver_tooth.habitat)
    # Second object
    lone_wolf = Wolf("Lone Wolf", 8)
    # Print out instance variable name
    print(lone_wolf.name)
    # Print out class variable classification
    print(lone_wolf.classification)


main()
