import enum


# compares a single attribute of three given cards, to check generically, if they are all different, or all the same
def same_or_different(num1, num2, num3):
    if num1 == num2 == num3 or (num1 != num2 != num3 != num1):
        return True
    return False


# preforms a generic check over the four attributes of a card, for the three given cards. returns true if theres a match
def match(card1, card2, card3):
    # I wanted to iterate over the attributes, but I can't use a variable as an attribute, maybe Mor knows how
    # for field in card1.__dict__:
    #   if not same_or_different(card1.field, card2.field, card3.field):
    #       return False
    # return True
    color = same_or_different(card1.color, card2.color, card3.color)
    shape = same_or_different(card1.shape, card2.shape, card3.shape)
    shading = same_or_different(card1.shading, card2.shading, card3.shading)
    num = same_or_different(card1.number, card2.number, card3.number)
    return color and shape and shading and num


# in the future we will make this with a dynamic programming algorithm
def set_algo_for_loop(cards):
    for card1 in cards[0:7]:
        for card2 in cards[1:8]:
            for card3 in cards[2:9]:
                if match(card1, card2, card3):
                    return card1.name, card2.name, card3.name


# all of out enums
class Color(enum.Enum):
    GREEN = 1
    RED = 2
    PURPLE = 3


class Shading(enum.Enum):
    SOLID = 1
    STRIPED = 2
    EMPTY = 3


class Number(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Shape(enum.Enum):
    DIAMOND = 1
    SQUIGGLE = 2
    OVAL = 3


class Card:
    def __init__(self, color, shading, number, shape, val):
        self.color = color
        self.shading = shading
        self.number = number
        self.shape = shape
        self.name = "card" + str(val)


if __name__ == '__main__':
    # example cards
    card1 = Card(Color.GREEN, Shading.STRIPED, Number.ONE, Shape.SQUIGGLE, 1)
    card2 = Card(Color.RED, Shading.EMPTY, Number.ONE, Shape.DIAMOND, 2)
    card3 = Card(Color.GREEN, Shading.SOLID, Number.THREE, Shape.OVAL, 3)
    card4 = Card(Color.RED, Shading.STRIPED, Number.TWO, Shape.SQUIGGLE, 4)
    card5 = Card(Color.PURPLE, Shading.EMPTY, Number.ONE, Shape.DIAMOND, 5)
    card6 = Card(Color.RED, Shading.SOLID, Number.ONE, Shape.OVAL, 6)
    card7 = Card(Color.PURPLE, Shading.STRIPED, Number.THREE, Shape.SQUIGGLE, 7)
    card8 = Card(Color.PURPLE, Shading.EMPTY, Number.ONE, Shape.DIAMOND, 8)
    card9 = Card(Color.RED, Shading.SOLID, Number.TWO, Shape.OVAL, 9)

    cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9]

    print(set_algo_for_loop(cards))
