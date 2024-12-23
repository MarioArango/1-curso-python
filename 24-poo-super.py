class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello! I am a person')

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        super().greet()
        print(f'Hello, my studen ID is {self.student_id}')

mario = Student('Mario', 29, '001')
mario.greet()