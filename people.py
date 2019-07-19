class Person: 
    def __init__(self, name, greeting): 
        self.name = name 
        self.greeting = greeting 
    def __str__(self): 
        return f'{self.name} {self.greeting}'

class Student(Person): 
    def __init__(self, name, greeting):
        super().__init__(name, greeting)
        return

    def learn(self): 
        return "I get it!" 

class Instructor(Person): 
    def __init__(self, name, greeting):
        super().__init__(name, greeting)
        return 

    def teach(self): 
        return "An object is an instance of a class" 
    


nadia = Instructor('Nadia', 'Hello, class!')
chris = Student('Chris', "Hey, class!")

print(nadia) 
print(chris) 
print()
print(nadia.teach())
print(chris.learn())
print() 
# chris.teach() ## student does not have an instance method "teach" 



