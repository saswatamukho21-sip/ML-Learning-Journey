class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def eat(self):
        print(f"{self.name} is eating!")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,"Woof")

    def learned_trick(self,trick):
        print(f"{self.name} learned {trick}")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name,"Meow")

    def purr(self):
        print(f"{self.name} is purring")

dog=Dog("Piglu")
dog.speak()
dog.eat()
dog.learned_trick("sit")

cat=Cat("Tom")
cat.speak()
cat.eat()
cat.purr()
        
