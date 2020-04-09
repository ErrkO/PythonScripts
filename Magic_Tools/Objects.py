class Card:
    cardID = 0
    cmc = 0
    colors = []
    mana_cost = ''
    name = ''
    power = ''
    rarity = ''
    set = ''
    subtypes = []
    text = ''
    toughness = ''
    type = []

    def __init__(self,card):
        self.cardID = card.cardID
        self.cmc = card.cmc
        self.colors = card.colors
        self.mana_cost = card.mana_cost
        self.name = card.name
        self.power = card.power
        self.rarity = card.rarity
        self.set = card.set
        self.subtypes = card.subtypes
        self.text = card.text
        self.toughness = card.toughness
        self.type = card.type

class Color:
    ColorID = 0
    ColorName = ''

    def __init__(self,color):
        self.ColorID = color.ColorID
        self.ColorName = color.ColorName

class Type:
    TypeID = 0
    TypeDesc = ''

    def __init__(self,type):
        self.TypeID = type.TypeID
        self.TypeDesc = type.TypeDesc

class Subtype:
    SubtypeID = 0
    SubtypeDesc = ''

    def __init__(self,subtype):
        self.SubtypeID = subtype.SubtypeID
        self.SubtypeDesc = subtype.SubtypeDesc

class Set:
    SetID = 0
    SetCode = ''
    SetName = ''

    def __init__(self,set):
        self.SetID = set.SetID
        self.SetCode = set.SetCode
        self.SetName = set.SetName
