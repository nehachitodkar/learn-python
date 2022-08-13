#!/usr/bin/python

class Parrot:


    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is {}".format(blu.__class__.species))
print("Woo is also {}".format(woo.__class__.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


