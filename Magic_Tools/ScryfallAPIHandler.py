import requests
import json
import PercentEncoder as Encoder
import Objects

card_url = 'https://api.scryfall.com/cards/'
set_url = 'https://api.scryfall.com/sets/'
abilities_url = 'https://api.scryfall.com/catalog/keyword-abilities'
actions_url = 'https://api.scryfall.com/catalog/keyword-actions'
Rarities = ['Common','Uncommon','Rare','Mythic']
formats = [ 'Standard','Commander','Duel','Legacy'
	        ,'Modern','Pioneer','Vintage','Pauper'
	        ,'Brawl','Future','Historic','Oldschool'
            ,'Penny' ]

def ConvertRequestToJson(rqst):
    response = requests.get(rqst)

    if response.status_code == 404:
        ThrowError(response.status_code)
    else:
        data = response.json()
        return data

def ConvertJsonToKeywords(json):
    pass

def ConvertJsonToCard(json):

    hjson = []
    
    if json.get("card_faces",'') != '':
        hjson = HandleSplitCard(json)
    else:
        hjson = HandleSingleCard(json)
        
    card = Objects.Card(0,hjson["cmc"],hjson["color_identity"],hjson["image_uris"]
                ,hjson["legalities"],hjson["mana_cost"],hjson["mechanics"],hjson["name"],hjson["collector_number"]
                ,hjson["power"],hjson["rarity"],hjson["set"],hjson["subtypes"],hjson["text"]
                ,hjson["toughness"],hjson["types"])

    return card

def HandleSplitCard(json):
    types = []
    subtypes = []
    name = ""
    mana_cost = ""
    text = ""
    power = ""
    toughness = ""

    for face in json["card_faces"]:
        tempTypes = face["type_line"]
        splits = tempTypes.split(' — ')
        types.extend(splits[0].split(' '))

        if len(splits) > 1:
            subtypes.extend(splits[1].split(' '))

        name += face["name"] + " // "
        mana_cost += face["mana_cost"] + " // "
        text += face["oracle_text"] + " // "
        
        if face.get("power",'') != '':
            power += face["power"] + " // "
            toughness += face["toughness"] + " // "
        else:
            power += ""
            toughness += ""
    
    if json.get("uri",'') != '':
        uri = json["uri"]
    else:
        uri = json["image_uris"]["normal"]

    legalities = []
    
    for form in formats:
        legalities.append([form,json['legalities'][form.lower()]])

    newJson = {
         "cmc":json["cmc"]
        ,"color_identity":json["color_identity"]
        ,"image_uris":uri
        ,"legalities":legalities
        ,"mana_cost":mana_cost[:-4]
        ,"mechanics": []
        ,"name":name[:-4]
        ,"collector_number":json["collector_number"]
        ,"power":power[:-4]
        ,"rarity":json["rarity"]
        ,"set":json["set"]
        ,"subtypes":subtypes
        ,"text":text[:-4]
        ,"toughness":toughness[:-4]
        ,"types":types
    }

    return newJson

def HandleSingleCard(json):
    types = json["type_line"]
    splits = types.split(' — ')

    types = splits[0]
    types = types.split(' ')

    if len(splits) > 1:
        subtypes = splits[1]
        subtypes = subtypes.split(' ')
    else:
        subtypes = []

    power = 'none'
    toughness = 'none'

    for typee in types:    
        if typee == 'Creature':
            power = json["power"]
            toughness = json["toughness"]
    
    if power == 'none' or toughness == 'none':
        power = None
        toughness = None

    legalities = []
    
    for form in formats:
        legalities.append([form,json['legalities'][form.lower()]])

    newJson = {
         "cmc":json["cmc"]
        ,"color_identity":json["color_identity"]
        ,"image_uris":json["image_uris"]["normal"]
        ,"legalities":legalities
        ,"mana_cost":json["mana_cost"]
        ,"mechanics": []
        ,"name":json["name"]
        ,"collector_number":json["collector_number"]
        ,"power":power
        ,"rarity":json["rarity"]
        ,"set":json["set"]
        ,"subtypes":subtypes
        ,"text":json["oracle_text"]
        ,"toughness":toughness
        ,"types":types
    }

    return newJson

def ConvertJsonToSet(json):
    pass

def GetAllSets():
    sets = []

    request = BuildQuery(set_url,'')
    lst_json = ConvertRequestToJson(request)
    sets.extend(lst_json["data"])

    for sett in sets:
        pass

def GetAllSetsInArena():
    pass

def BuildQuery(url,params):
    parser = Encoder.PercentEncoder()
    query = parser.ParseString(params)
    return url + 'search?order=set&q=' + query

def GetAllCardsInSet(setcode):
    mtgcards = []
    cards = []

    for rarity in Rarities:
        set_str = 'set:' + setcode
        rarity_str = 'r=' + rarity
        q = set_str + ' ' + rarity_str

        request = BuildQuery(card_url,q)

        lst_json = ConvertRequestToJson(request)

        mtgcards.extend(lst_json["data"])

    for mtgcard in mtgcards:
        cards.append(ConvertJsonToCard(mtgcard))

    return cards

def GetAllCardsInArena():
    mtgcards = []
    cards = []

    q = 'game=arena'

    request = BuildQuery(card_url,q)
    lst_json = ConvertRequestToJson(request)

    mtgcards.extend(lst_json["data"])

    while lst_json["has_more"]:
        request_next = lst_json["next_page"]
        lst_json = ConvertRequestToJson(request_next)
        mtgcards.extend(lst_json["data"])

    for card in mtgcards:
        cards.append(ConvertJsonToCard(card))

    return cards

def GetAllSubtypes(isCardsLoaded,*argv):
    if isCardsLoaded:
        cards = argv[0]
    else:
        cards = GetAllCardsInArena()

    subtypes = []
    
    for card in cards:
        if IsCreature(card):
            for stype in card.subtypes:
                if IsNotInList(stype,subtypes):
                    subtypes.append(stype)

    return subtypes

def GetAllKeywords():
    keywords = []
    abilities = ConvertRequestToJson(abilities_url)
    actions = ConvertRequestToJson(actions_url)

    for ability in abilities["data"]:
        keywords.append(ability)

    for action in actions["data"]:
        keywords.append(action)

    return keywords

def IsNotInList(comparable,lst):
    for item in lst:
        if comparable == item:
            return False
    return True

def IsSubList(item):
    if len(item) > 1:
        return True
    return False

def FlattenList(lst):
    flatLst = []
    for item in lst:
        if IsSubList(item):
            for it in item:
                flatLst.append(it)
        else:
            flatLst.append(item)
    return flatLst

def IsCreature(card):
    for ttype in card.type:
        if ttype == "Creature":
            return True
    return False

def ThrowError(status_code):
    if status_code == 404:
        print('404 - Request Not Found!')

#request = 'https://api.scryfall.com/cards/search?order=set&q=set%3Athb+r%3DCommon'

#cards = GetAllCardsInSet('thb')

#cards = GetAllCardsInArena()

# GetAllSubtypes(True,cards)

#keywords = GetAllKeywords()

#print('')

#obj_json = ConvertRequestToJson(request)

#print(obj_json)
