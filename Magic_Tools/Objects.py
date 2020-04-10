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

    def __init__(self,*argv):
        if type(argv[0]) is Card:
            card = argv[0]
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
        else:
            self.cardID = argv[0]
            self.cmc = argv[1]
            self.colors = argv[2]
            self.mana_cost = argv[3]
            self.name = argv[4]
            self.power = argv[5]
            self.rarity = argv[6]
            self.set = argv[7]
            self.subtypes = argv[8]
            self.text = argv[9]
            self.toughness = argv[10]
            self.type = argv[11]

    def Parameterize(self):
        return ([self.cardID,self.cmc,self.colors,self.mana_cost
                    ,self.name,self.power,self.rarity,self.set
                    ,self.subtypes,self.text,self.toughness,self.type,])

class Color:
    ColorID = 0
    ColorName = ''

    def __init__(self,*argv):
        if type(argv[0]) is Color:
            color = argv[0]
            self.ColorID = color.ColorID
            self.ColorName = color.ColorName
        else:
            self.ColorID = argv[0]
            self.ColorName = argv[1]

    def Parameterize(self):
        return ([self.ColorID,self.ColorName,])

class Type:
    TypeID = 0
    TypeDesc = ''

    def __init__(self,*argv):
        if type(argv) is Type:
            self.TypeID = argv[0].TypeID
            self.TypeDesc = argv[0].TypeDesc
        else:
            self.TypeID = argv[0]
            self.TypeDesc = argv[1]

    def Parameterize(self):
        return ([self.TypeID,self.TypeDesc,])

class Subtype:
    SubtypeID = 0
    SubtypeDesc = ''

    def __init__(self,*argv):
        if type(argv) is Subtype:
            subtype = argv[0]
            self.SubtypeID = subtype.SubtypeID
            self.SubtypeDesc = subtype.SubtypeDesc
        else:
            self.SubtypeID = argv[0]
            self.SubtypeDesc = argv[1]

    def Parameterize(self):
        return ([self.SubtypeID,self.SubtypeDesc,])

class Set:
    SetID = 0
    SetCode = ''
    SetName = ''

    def __init__(self,*argv):
        if type(argv[0]) is Set:
            self.SetID = argv[0].SetID
            self.SetCode = argv[0].SetCode
            self.SetName = argv[0].SetName
        else:
            self.SetID = argv[0]
            self.SetCode = argv[1]
            self.SetName = argv[2]

    def Parameterize(self):
        return ([self.SetID,self.SetCode,self.SetName,])
