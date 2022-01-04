class Animal:
    def __init__(self, name, animalClass, weight):
        self.name = name
        self.animalClass = animalClass
        self.weight = weight
    
    def showDescription(self):
        print(f"This animal is a {self.name}, a type of {self.species}, and has a weight of {self.weight}")
    
    def getName(self):
        print(f"Getting name")
        return self.name
    
    def setName(self, name):
        print(f"Setting name")
        self.name = name
    
    def move(self):
        print(f"{self.name} is moving")
        
    def eat(self):
        print(f"Eating")
        print(f"{self.name} is now nourished")
        
    def rest(self):
        print(f"Resting")
        print(f"{self.name} is now rested")
        
    def procreate(self):
        print(f"Procreating")
        print(f"There is now more of {self.name}")

class Fish(Animal):
    def __init__(self, name, animalClass, weight, species, freshWater):
        super().__init__(name, animalClass, weight)
        self.species = species
        self.freshWater = freshWater
        
    def swim(self):
        print(f"{self.name} is swimming in the water")

class Snake(Animal):
    def __init__(self, name, animalClass, weight, species, length, venomous):
        super().__init__(name, animalClass, weight)
        self.species = species
        self.length = length
        self.venomous = venomous
    
    def hibernate(self):
        print(f"{self.name} is hibernating for the season")
    
    def slither(self):
        print(f"{self.name} is slithering on the ground")

class Person(Animal):
    def __init__(self, name, animalClass, weight, age, ethnicity):
        super().__init__(name, animalClass, weight)
        self.age = age
        self.ethnicity = ethnicity
        
    def sleep(self):
        print(f"{self.name} has fallen asleep and won't be up for a few hours")
        
    def walk(self):
        print(f"{self.name} is walking around")

class Book:
    def __init__(self, title, author, pages, yearPublished):
        self.title = title
        self.author = author
        self.pages = pages
        self.yearPublished = yearPublished
        
    def showDescription(self):
        print(f"This book is titled '{self.title}', which was written by {self.author} in {self.yearPublished}, and has {self.pages} pages in it.")
        
    def getTitle(self):
        print(f"Getting title")
        return self.title
    
    def setTitle(self, title):
        print(f"Setting title")
        self.title = title
    
    def open(self):
        print(f"Opening '{self.title}'")
        
    def read(self):
        print(f"Reading '{self.title}'")
        
    def close(self):
        print(f"Closing '{self.title}'")

class Textbook(Book):
    def __init__(self, title, author, pages, yearPublished, ISBN, subject, publisher):
        super().__init__(title, author, pages, yearPublished)
        self.ISBN = ISBN
        self.subject = subject
        self.publisher = publisher
        
    def answerQuestion(self):
        print(f"Answering questions from the textbook")

class AddressBook(Book):
    def __init__(self, title, author, pages, yearPublished, contactName, postalAddress, phoneNumber, notes):
        super().__init__(title, author, pages, yearPublished)
        self.contactName = contactName
        self.postalAddress = postalAddress
        self.phoneNumber = phoneNumber
        self.notes = notes
    
    def enterInfo(self, contactName, postaladdress, phoneNumber, notes):
        print(f"{self.contactName}, {self.postalAddress}, and {self.phoneNumber} have been added to the book")
    
    def deleteInfo(self, contactName, postaladdress, phoneNumber, notes):
        print(f"{self.contactName}, {self.postalAddress}, and {self.phoneNumber} have been deleted from the book")
 

class Vehicle:
    def __init__(self, name, color, style, capacity, year):
        self.name = name
        self.color = color
        self.style = style
        self.capacity = capacity
        self.year = year
        
    def showDescription(self):
        print(f"This vehicle is a {self.name}, which is a {self.color} {self.style} made in {self.year}, and has a capacity of {self.capacity} seats.")
        
    def getName(self):
        print(f"Getting name")
        return self.name
    
    def setName(self, name):
        print(f"Setting name")
        self.name = name
        
    def setColor(self, color):
        print(f"Changing color")
        self.color = color
        
    def move(self):
        print(f"{self.name} is now in motion")
        
class Car(Vehicle):
    def __init__(self, name, color, style, capacity, year, mileage, manufacturer):
        super().__init__(name, color, style, capacity, year)
        self.mileage = mileage
        self.manufacturer = manufacturer
        
    def startEngine(self):
        print(f"{self.name} has been started")
        
    def drive(self):
        print(f"{self.name} is now in motion")
        
    def brake(self):
        print(f"{self.name} has slowed down")
        
    def stopEngine(self):
        print(f"{self.name} has stopped")

class Bicycle(Vehicle):
    def __init__(self, name, color, style, capacity, year, material):
        super().__init__(name, color, style, capacity, year)
        self.material = material
        
    def pedal(self):
        print(f"{self.name} is in motion")
        
    def brake(self):
        print(f"{self.name} has slowed down and may have stopped")

class Boat(Vehicle):
    def __init__(self, name, color, style, capacity, year, type):
        super().__init__(name, color, style, capacity, year)
        self.type = type
        
    def startEngine(self):
        print(f"{self.name} has been started")
        
    def drive(self):
        print(f"{self.name} is now in motion")
        
    def brake(self):
        print(f"{self.name} has slowed down")
        
    def stopEngine(self):
        print(f"{self.name} has stopped")

class HotAirBalloon(Vehicle):
    def __init__(self, name, color, style, capacity, year, altitude):
        super().__init__(name, color, style, capacity, year)
        self.altitude = altitude
    
    def takeoff(self):
        print(f"{self.name} has taken off the ground")
        
    def fly(self):
        print(f"{self.name} is moving in the air")
        
    def increaseAltitude(self):
        print(f"{self.name} has gone higher in the air")
        
    def decreaseAltitude(self):
        print(f"{self.name} has lowered from the sky")
        
    def land(self):
        print(f"{self.name} has landed on the ground")