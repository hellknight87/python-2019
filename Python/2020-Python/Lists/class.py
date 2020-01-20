class Human:
    # instance attributes
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        
    # instance methonds (behaviours)
    def eating(self, food):
        return "{} is eating {}".format(self.name, food)


# creating objects of class human
ram = Human("Ram" ,6 ,60)
steve = Human("Steve", 5.9, 56)

# accessing object information

print("Height of {} is {}".format(ram.name, ram.height))
print("Weight of {} is {}".format(ram.name, ram.weight))
print(ram.eating("Pizza"))
print("Height of {} is {}".format(steve.name, steve.height))
print("Weight of {} is {}".format(steve.name, steve.weight))
print(steve.eating("Big Kahuna Burger"))