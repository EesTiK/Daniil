class Dog ():
    age = 5
    name = "Charly"
    weight = 15
toyterier = Dog()
toyterier.age = 5
toyterier.name = "Charly"
toyterier.weight = 15
#----------------------------------------------------
class Person():
    name = "Jegor"
    cellphone = "2281337"
    email = "blablala@mail.ru"
#-----------------------------------------------------
class bird():
    color = " "
    name = " "
    breed = " "
mybird = bird ()
mybird.color = "black"
mybird.name = "Sunny"
mybird.breed = "Sun Conure"
#-------------------------------------------------------------
class Hero:
    power = " "
    name = " "
    agility = " "
    speed = " "
#------------------------------------------------------------------
class Peson:
    name = ""
    money = 0

bob = Person ()
bob.name = "bob"
bob.money = 0
print (bob.name, "has", "dollars.")
#---------------------------------------------------------------
x = 0
y = 0
mainhero = Hero()
mainhero.x = 3939
mainhero.y = 3030
mainhero.name = "Blaka"
mainhero.power = 39
mainhero.agility = 90
mainhero.speed = 20
#--------------------------------------------
class Person:
    name = " "
    money = 0
    
bob = Person ()
name = "Bla"
money = 1080
#--------------------------------------------
class cow ():
    age = 17
    name = "Bob"
    weight = 61
#------------------------------------------
import time
class Cat():
   
    def __init__ (self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
       
    def info(self):
        time.sleep(0.5)
        print( "Имя: " + self.name )
        time.sleep(0.7)
        print( "Цвет: " + self.color )
        time.sleep(0.8)
        print( "Вес: " + str( self.weight ) )
       
    def meow(self):
        print( self.name + ", лег(-ла) спать..." )
        time.sleep(0.6)
        print( self.name + " мурлычит..." )
       
cot = Cat( "Котёнок - Царь","Брюнет",300)
cot.info()
cot.meow()
    