
class Animal:
    def __init__(self, name):  
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed
    
    def speak(self):
        return f"{self.name}, the {self.breed}, barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak()) 
