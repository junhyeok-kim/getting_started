from random import choice
import numpy as np
import pandas as pd


class Person:

    def __init__(self, name):
        self.greeting = '<div>Hello {name}</div>'  # inject HTML language
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name)


def main():
    people = [
        Person('Jane'),
        Person('Jill'),
        Person('Bob')
    ]
    person = choice(people)
    print(person)

if __name__ == '__main__':
    print('hello')
    main()
