#!/usr/bin/env python3

class Dog:
    def __init__(self, name, favorite_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy

fido = Dog("Fido")
fido.favorite_toy

snoopy = Dog("Snoopy", "Tennis Ball")
snoopy.favorite_toy