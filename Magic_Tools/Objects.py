class Card:
    cardID = 0
    cmc = 0
    colors = []
    ImageURL = ''
    mana_cost = ''
    name = ''
    number = ''
    power = ''
    rarity = ''
    setCode = ''
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
            self.ImageURL = card.ImageURL
            self.mana_cost = card.mana_cost
            self.name = card.name
            self.number = card.number
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
            self.ImageURL = argv[3]
            self.mana_cost = argv[4]
            self.name = argv[5]
            self.number = argv[6]
            self.power = argv[7]
            self.rarity = argv[8]
            self.set = argv[9]
            self.subtypes = argv[10]
            self.text = argv[11]
            self.toughness = argv[12]
            self.type = argv[13]

    def Parameterize(self,skipID = False):
        if skipID == True:
            return ([self.cmc,self.colors,self.ImageURL,self.mana_cost
                    ,self.name,self.number,self.power,self.rarity,self.set
                    ,self.subtypes,self.text,self.toughness,self.type,])
        return ([self.cardID,self.cmc,self.colors,self.ImageURL,self.mana_cost
                    ,self.name,self.number,self.power,self.rarity,self.set
                    ,self.subtypes,self.text,self.toughness,self.type,])

    def __str__(self):
        return self.name + ' (' + self.setCode + ') ' + self.number

    def __gt__(self,c2):
        if self.ParseNumber() > c2.ParseNumber():
            return True
        else:
            return False
    
    def __ge__(self,c2):
        if self.ParseNumber() >= c2.ParseNumber():
            return True
        else:
            return False

    def __lt__(self,c2):
        if self.ParseNumber() < c2.ParseNumber():
            return True
        else:
            return False

    def __le__(self,c2):
        if self.ParseNumber() <= c2.ParseNumber():
            return True
        else:
            return False

    def __eq__(self,c2):
        if self.ParseNumber() == c2.ParseNumber():
            return True
        else:
            return False

    def ParseNumber(self):
        number = self.number
        if number.isnumeric():
            return int(number)

        lst = self.Split()
        nlst = ''

        for char in lst:
            if char.isnumeric():
                nlst += char

        return int(nlst)

    def Split(self): 
        return [char for char in self.number]  

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

    def Parameterize(self,skipID = False):
        if skipID == True:
            return ([self.ColorName,])    
        return ([self.ColorID,self.ColorName,])

class ColorIdentity:
    CIdentityID = 0
    CIDentityName = ''
    CIdentitySymbol = ''

    def __Init__(self,*argv):
        if type(argv[0]) is ColorIdentity:
            cidentity = argv[0]
            self.CIdentityID = cidentity.CIdentityID
            self.CIDentityName = cidentity.CIDentityName
            self.CIdentitySymbol = cidentity.CIdentitySymbol
        else:
            self.CIdentityID = argv[0]
            self.CIDentityName = argv[1]
            self.CIdentitySymbol = argv[2]

    def Parameterize(self,skipID = False):
        if skipID == True:
            return ([self.CIDentityName,self.CIdentitySymbol,])
        return ([self.CIdentityID,self.CIDentityName,self.CIdentitySymbol,])
    
    def __str__(self):
        return self.CIDentityName + ' - ' + self.CIdentitySymbol

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

    def Parameterize(self,skipID = False):
        if skipID == True:
            return ([self.TypeDesc,])
        return ([self.TypeID,self.TypeDesc,])

class Subtype:
    SubtypeID = 0
    SubtypeDesc = ''

    def __init__(self,*argv):
        if type(argv[0]) is Subtype:
            subtype = argv[0]
            self.SubtypeID = subtype.SubtypeID
            self.SubtypeDesc = subtype.SubtypeDesc
        else:
            self.SubtypeID = argv[0]
            self.SubtypeDesc = argv[1]

    def Parameterize(self,skipID = False):
        if skipID == True:
            return ([self.SubtypeDesc,])
        return ([self.SubtypeID,self.SubtypeDesc,])

class Supertype:
    SupertypeID = 0
    SupertypeDesc = ''

    def __init__(self,*argv):
        if type(argv[0]) is Supertype:
            supertype = argv[0]
            self.SupertypeID = supertype.SupertypeID
            self.SupertypeDesc = supertype.SupertypeDesc
        else:
            self.SupertypeID = argv[0]
            self.SupertypeDesc = argv[1]

    def Parameterize(self,skipID = False):
        if skipID == True:
            return ([self.SupertypeDesc,])
        return ([self.SupertypeID,self.SupertypeDesc,])

class Set:
    SetCode = ''
    SetName = ''

    def __init__(self,*argv):
        if type(argv[0]) is Set:
            self.SetCode = argv[0].SetCode
            self.SetName = argv[0].SetName
        else:
            self.SetCode = argv[1]
            self.SetName = argv[2]

    def Parameterize(self,skipID = False):
        return ([self.SetCode,self.SetName,])
