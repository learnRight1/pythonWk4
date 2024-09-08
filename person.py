# Define the Person class
class Person:
    # Constructor to initialize attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Ezekiel Samuel", 25, "Male")

# Call the introduce method
person1.introduce()
