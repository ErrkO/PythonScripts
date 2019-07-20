import random

class Card:

    cardTypes = ["Spell","Land"]

    cardValue = ""

    def __init__():
        index = random.randint(0,1)
        cardValue = cardTypes[index]

    def __init__(typeID):
        cardValue = cardTypes[typeID]

class Stack:

    stack = []

    def __init__():
        stack = []

    def pop():
        size = len(stack) - 1
        value = stack[size]
        del stack[-1]
        return value

    def popAt(index):
        value = stack[index]
        del stack[index]
        return value
    
    def push(value):
        stack.extend(value)

    def pushRange(lst):
        stack.extend(lst)

    
class Shuffler:

    def randomShuffle(deck):
        newDeck = Stack()

        while len(deck) != 0:
            newDeck.push(deck.pop())

        return newDeck

    def pileShuffle(deck):
        pile1 = Stack()
        pile2 = Stack()
        pile3 = Stack()
        pile4 = Stack()
        pile5 = Stack()

        size = len(deck) - 1

        for i = 0 in range(size):

            if i % 5 == 0:
                pile1.push(deck.pop())

            elif i % 5 == 1:
                pile2.push(deck.pop())

            elif i % 5 == 2:
                pile3.push(deck.pop())

            elif i % 5 == 3:
                pile4.push(deck.pop())

            elif i % 5 == 4:
                pile5.push(deck.pop())