class Animal():
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Meow")
    
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Bark")

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__persons = []
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
     
    #   @property   making fun act like property
    #   def age():
    #       return self.__age
                            
    def get_age(self):    
        return self.__age 
    
    #   age.setter
    def set_age(self, new_age):
        self.__age = new_age
    
    def get_total_people(self):
        return self.__persons

    def total_people(self):
        for person in self.persons:
            print(person.get_name())


    def introduce(self):
        print(f"My name is {self.__name}, i'm {self.__age} old")


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def teach(self):
        print(f"{self.get_name()} is teaching")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.get_name()} is study")

if __name__ == "__main__":
    # c = Cat()
    # d = Dog()
    # c.make_sound()
    # d.make_sound()
    # student_id = 0
    # time = 0
    p1 = Teacher("Anna", 32)
    p2 = Teacher("Julia", 44)
    p3 = Teacher("Mark", 56)
    p4 = Teacher("Marks", 31)
    p4.get_total_people()
    # s1 = Student("Richard", 22, 1)
    # s2 = Student("Mike", 21, 2)
    # s3 = Student("Gale", 23, 3)
    # s4 = Student("John", 24, 4)
    # students = [s1, s2, s3, s4]
    # teachers = [t1, t2, t3, t4]
    # while time < 4:
    #     time += 1
    #     for teacher in teachers:
    #         teacher.introduce()
    #         for student in students:
    #             student.introduce()
    #             teacher.teach()
    #             student.study()

