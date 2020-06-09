import requests
import json
import PercentEncoder as Encoder
import Objects

card_url = 'https://api.scryfall.com/cards/'
set_url = 'https://api.scryfall.com/sets/'
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

def ConvertJsonToCard(json):
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

    if json["oracle_text"] 

    card = Objects.Card(0,json["cmc"],json["color_identity"],json["image_uris"]["normal"]
                ,legalities,json["mana_cost"],json["name"],json["collector_number"],power
                ,json["rarity"],json["set"],subtypes,json["oracle_text"],toughness
                ,types)

    return card

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
        
def ThrowError(status_code):
    if status_code == 404:
        print('404 - Request Not Found!')

#request = 'https://api.scryfall.com/cards/search?order=set&q=set%3Athb+r%3DCommon'

#cards = GetAllCardsInSet('thb')

cards = GetAllCardsInArena()

print('')

#obj_json = ConvertRequestToJson(request)

#print(obj_json)
