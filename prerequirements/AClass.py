import random


class Animal(object):
    def __init__(self, age):
        assert type(age) == int
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newAge):
        self.age = newAge

    def set_name(self, newName="Hasan"):
        self.name = newName

    def __str__(self):
        return "Animal: " + str(self.name) + " : " + str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat: " + str(self.name) + " : " + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friend(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), " year difference")

    def __str__(self):
        return "Person: " + str(self.name) + " : " + str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")

        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching tv")

    def __str__(self):
        return "Student: " + str(self.name) + " : " + str(self.age) + " : " + str(self.major)


class Rabbit(Animal):
    tag = 1  # class variable

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag  # rid is an instance variable
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid

        parents_opposite = self.parent2.rid == other.parent2.rid and self.parent1.rid == other.parent2.rid

        return parents_same or parents_opposite


myAnimal = Animal(3)
print(myAnimal.name)
print(myAnimal.get_age())
print(myAnimal.age)
myAnimal.size = 5
print(myAnimal.size)

myAnimal.set_name("Ali")
print(myAnimal.get_name())

cat = Cat(25)
cat.set_name("Tom")
print(str(cat.get_age()) + "\n")
print(cat)

print("\n----- Person tests-------\n")
p1 = Person("Jack", 30)
p2 = Person("jill ", 25)

print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)

print("\n -----student tests------")
s1 = Student('alice', 20, "CS")
s2 = Student("beth", 18)

print(s1)

print(s2)

print(s1.get_name(), "says", end=" ")
s1.speak()
print(s2.get_name(), " says: ", end=" ")
s2.speak()

r1 = Rabbit(25)
print(r1.rid)
r2 = Rabbit(2)
print(r2.rid)
r3 = r1 + r2
print("r3: ", r3.get_rid())
r4 = r2 + r1

r5=r3+r4
r6=r4+r3
print(str(r5.__eq__(r6)) + " and : " + str(r6.__eq__(r5)))
