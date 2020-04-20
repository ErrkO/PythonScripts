import requests
import json
import PercentEncoder as Encoder
import Objects

card_url = 'https://api.scryfall.com/cards/'
set_url = 'https://api.scryfall.com/sets/'
Rarities = ['Common','Uncommon','Rare','Mythic']

def ConvertRequestToJson(rqst):
    response = requests.get(rqst)

    if response.status_code == 404:
        ThrowError(response.status_code)
    else:
        data = response.json()
        for dat in data.data:
            print('')
        return json.loads(data.data)

def GetAllSets():
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
        request = BuildQuery(card_url,set_str + ' ' + rarity_str)

        lst_json = ConvertRequestToJson(request)

        mtgcards.extend(lst_json.data)

    for mtgcard in mtgcards:
        types = mtgcard.type_line
        types = types.split(' - ')[1]
        subtypes = types.split(' ')

        card = Objects.Card(0,mtgcard.cmc,mtgcard.color_identity,mtgcard.image_uris.normal,mtgcard.mana_cost
                    ,mtgcard.name,mtgcard.collector_number,mtgcard.power,mtgcard.rarity,mtgcard.set
                    ,mtgcard.subtypes,mtgcard.oracle_text,mtgcard.toughness,mtgcard.types)
        cards.append(card)

    #SortCards(cards)

    return cards
        
def ThrowError(status_code):
    if status_code == 404:
        print('404 - Request Not Found!')

request = 'https://api.scryfall.com/cards/search?order=set&q=set%3Athb+r%3DCommon'

cards = GetAllCardsInSet('thb')

obj_json = ConvertRequestToJson(request)

print(obj_json)
